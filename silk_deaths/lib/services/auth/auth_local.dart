// lib/services/auth_service.dart

import 'package:silk_deaths/enums/auth_status.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../../models/User.dart';

/// Serviço (Service/Repository) para gerenciar operações de DB para autenticação.
class AuthLocal {
  // --- Implementação do Padrão Singleton ---
  static final AuthLocal _instance = AuthLocal._internal();
  factory AuthLocal() => _instance;
  AuthLocal._internal();
  // --- Fim do Singleton ---

  Database? _database;
  final String _tableName = 'users';
  final String _dbName = 'auth_database.db';

  // 1. Getter que garante que o banco de dados só seja inicializado uma vez.
  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDatabase();
    return _database!;
  }

  // 2. Inicializa o banco de dados (cria a conexão e a tabela, se não existir).
  Future<Database> _initDatabase() async {
    final databasePath = await getDatabasesPath();
    final path = join(databasePath, _dbName);

    return await openDatabase(
      path,
      version: 1,
      onCreate: (db, version) {
        // SQL: Comando para CRIAR a tabela.
        return db.execute(
          '''
          CREATE TABLE $_tableName(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE, 
            password TEXT
          )
          ''',
        );
      },
    );
  }

  Future<AuthStatus> registerUser(User user) async {
    try {
      final db = await database;
      final id = await db.insert(
        _tableName,
        user.toMap(),
        conflictAlgorithm: ConflictAlgorithm.fail,
      );
      print('Usuário inserido com ID: $id');
      return AuthStatus.success;
    }
    on DatabaseException catch (e) {
        if (e.isUniqueConstraintError()) {
          print('Erro de registro: E-mail já existe.');
          return AuthStatus.emailAlreadyExists;
        }
        print('Erro desconhecido do banco de dados: $e');
        return AuthStatus.unknownError;
    }
    catch (e) {
      print('Erro geral ao registrar: $e');
      return AuthStatus.unknownError;
    }
  }

  Future<User?> login(String email, String password) async {
    try {
      final db = await database;
      // SQL: Seleciona linhas onde o email E a password coincidem.
      final List<Map<String, dynamic>> maps = await db.query(
        _tableName,
        where: 'email = ? AND password = ?',
        whereArgs: [email, password], // Valores que substituem os '?' na ordem.
      );

      if (maps.isNotEmpty) {
        // Se a lista de resultados não for vazia, encontramos o usuário.
        // Usamos o método fromMap() para converter o Map de volta para um objeto User.
        return User.fromMap(maps.first);
      }
      return null;
    }
    catch(e){
      return null;
    }
  }

  /// 5. Recover password (Simulação - operação SELECT).
  // Future<String?> recoverpassword(String email) async {
  //   final db = await database;
  //   // Seleciona a coluna 'password' para o email fornecido.
  //   final List<Map<String, dynamic>> maps = await db.query(
  //     _tableName,
  //     columns: ['password'],
  //     where: 'email = ?',
  //     whereArgs: [email],
  //   );
  //
  //   if (maps.isNotEmpty) {
  //     return maps.first['password'] as String;
  //   }
  //   return null;
  // }
}