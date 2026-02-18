// lib/services/auth_service.dart

import 'dart:convert';

import 'package:flutter/services.dart';
import 'package:silk_deaths/enums/auth_status.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../../extensions/string_extensions.dart';
import '../../models/Monster.dart';
import '../../models/User.dart';

/// Serviço (Service/Repository) para gerenciar operações de DB para autenticação.
class AuthLocal {
  // --- Implementação do Padrão Singleton ---
  static final AuthLocal _instance = AuthLocal._internal();

  factory AuthLocal() => _instance;

  AuthLocal._internal();

  // --- Fim do Singleton ---

  Database? _globalUsersDb;
  Database? _userMonsterDb;
  int? _currentUserId;

  final String _tableGlobalUsersName = 'users.db';
  final String _tableMonstersNames = 'monsters';

  Future<Database> get globalUsersDatabase async {
    if (_globalUsersDb != null && _globalUsersDb!.isOpen) return _globalUsersDb!;
    _globalUsersDb = await _initGlobalDb();
    return _globalUsersDb!;
  }

  Future<Database> _initGlobalDb() async {
    final path = join(await getDatabasesPath(), _tableGlobalUsersName);
    return await openDatabase(
      path,
      version: 1,
      onCreate: (db, version) async {
        await db.execute('''
          CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE, 
            password TEXT
          )
        ''');
      },
    );
  }

  Future<Database> getuserMonsterDatabase(int userId) async {

    final databasePath = await getDatabasesPath();
    final path = join(databasePath, 'user_$userId.db');

    print("getuserMonsterDatabase");
    print("userId: $userId");
    print("databasePath: $databasePath");
    print("path: $path");

    if (_userMonsterDb != null && _userMonsterDb!.isOpen && _userMonsterDb!.path == path) {
      return _userMonsterDb!;
    }

    await _userMonsterDb?.close();

    _userMonsterDb = await openDatabase(
      path,
      version: 1,
      onCreate: (db, version) async {
        await db.execute('''
          CREATE TABLE monsters(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            regions TEXT,
            deaths INTEGER DEFAULT 0,
            boss INTEGER,
            optional INTEGER,
            act INTEGER
          )
        ''');

        final List<Map<String, dynamic>> rawJsonMonsters = await _loadMonstersFromJson();
        final batch = db.batch();
        for (final jsonMonsters in rawJsonMonsters) {
          batch.insert('monsters', Monster.fromJson(jsonMonsters).toMap());
        }
        await batch.commit();
      },
    );
    print("_userMonsterDb: $_userMonsterDb");
    return _userMonsterDb!;
  }

  Future<void> restoreSession(int userId) async {
    _currentUserId = userId;
    await getuserMonsterDatabase(userId);
  }

  Future<AuthStatus> registerUser(User user) async {
    final db = await globalUsersDatabase;
    try {
      await db.insert('users', user.toMap());
      return AuthStatus.success;
    } on DatabaseException catch (e) {
      if (e.isUniqueConstraintError()) return AuthStatus.emailAlreadyExists;
      return AuthStatus.unknownError;
    }
  }

  Future<User?> login(String email, String password) async {
    final db = await globalUsersDatabase;
    final List<Map<String, dynamic>> maps = await db.query(
      'users',
      where: 'email = ? AND password = ?',
      whereArgs: [email, password],
    );

    if (maps.isNotEmpty) {
      final loggedUser = User.fromMap(maps.first);
      _currentUserId = loggedUser.id;
      print("_currentUserId $_currentUserId");
      await getuserMonsterDatabase(loggedUser.id!);
      return loggedUser;
    }
    return null;
  }

  Future<List<Monster>> getMonsters() async {
    if (_currentUserId == null) return [];
    final db = await getuserMonsterDatabase(_currentUserId!);
    final List<Map<String, dynamic>> maps = await db.query('monsters', orderBy: 'name ASC');
    return maps.map((m) => Monster.fromMap(m)).toList();
  }

  Future<List<Map<String, dynamic>>> _loadMonstersFromJson() async {
    try {
      final jsonString = await rootBundle.loadString('assets/default_bosses.json');
      final Map<String, dynamic> jsonResponse = json.decode(jsonString);
      final List<dynamic> list = jsonResponse['monsters'];
      return list.cast<Map<String, dynamic>>();
    } catch (e) {
      return [];
    }
  }

  Future<void> updateMonster(Monster monster) async {
    if (_currentUserId == null) return;
    final db = await getuserMonsterDatabase(_currentUserId!);
    await db.update(
      _tableMonstersNames,
      monster.toMap(),
      where: 'id = ?',
      whereArgs: [monster.id],
    );
  }

  Future<void> logout() async {
    await _userMonsterDb?.close();
    _userMonsterDb = null;
    _currentUserId = null;
  }
}
