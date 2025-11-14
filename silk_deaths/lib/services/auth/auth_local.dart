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
    if (_database != null) {
      try {
        // Tenta uma query leve para validar
        await _database!.rawQuery('SELECT 1');
        return _database!;
      } on DatabaseException catch (e) {
        // <<< DETECTA O ERRO ESPECÍFICO >>>
        if (e.isReadOnlyError() || e.toString().contains('DBMOVED')) {
          print('DB corrompido ou deletado. Recriando...');
          await _database?.close();
          _database = null;
        } else {
          rethrow;
        }
      } catch (e) {
        await _database?.close();
        _database = null;
      }
    }

    _database = await _initDatabase();
    return _database!;
  }

  // 2. Inicializa o banco de dados (cria a conexão e a tabela, se não existir).
  Future<Database> _initDatabase() async {
    final databasePath = await getDatabasesPath();
    final path = join(databasePath, _dbName);
    final exists = await databaseExists(path);

    return await openDatabase(
      path,
      version: 1,
      onConfigure: (db) async {
        // Força permissão de escrita (crucial em alguns dispositivos)
        await db.execute('PRAGMA foreign_keys = ON');
      },
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
      onOpen: (db) async {
        // Opcional: validar estrutura, migrações, etc.
        print('Banco de dados aberto: $path');
      },
    );
  }

  Future<AuthStatus> registerUser(User user) async {
    try {
      final db = await database; // ← aqui ele tenta abrir/recriar se necessário

      final id = await db.insert(
        _tableName,
        user.toMap(),
        conflictAlgorithm: ConflictAlgorithm.fail,
      );
      print('Usuário inserido com ID: $id');
      return AuthStatus.success;
    } on DatabaseException catch (e) {
      // 1. EMAIL JÁ EXISTE
      if (e.isUniqueConstraintError()) {
        print('Erro de registro: E-mail já existe.');
        return AuthStatus.emailAlreadyExists;
      }

      // IMPORTANTE, ISSO AQUI É APENAS TESTE INTERNO QUANDO O ARQUIVO DE DB É PERDIDO
      //Se o arquivo não existe ou está corrompido → recrie do zero

      // 2. BANCO MORTO (arquivo deletado, readonly, movido)
      if (e.toString().contains('READONLY_DBMOVED') ||
          e.toString().contains('1032') ||
          e.toString().contains('attempt to write a readonly database')) {

        print('Banco corrompido ou deletado. Tentando recriar...');

        // FORÇA RECRIAÇÃO
        await resetDatabase(); // ← função que vamos criar agora

        // TENTA NOVAMENTE UMA VEZ
        try {
          final db = await database;
          final id = await db.insert(_tableName, user.toMap(), conflictAlgorithm: ConflictAlgorithm.fail);
          print('Usuário inserido após reset: $id');
          return AuthStatus.success;
        } catch (_) {
          return AuthStatus.databaseCorrupted;
        }
      }

      // 3. OUTROS ERROS DE DB
      print('Erro desconhecido do banco de dados: $e');
      return AuthStatus.unknownError;
    } catch (e) {
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

  Future<void> resetDatabase() async {
    try {
      await _database?.close();
      _database = null;

      final databasePath = await getDatabasesPath();
      final path = join(databasePath, _dbName);

      if (await databaseExists(path)) {
        await deleteDatabase(path);
        print('Banco antigo deletado: $path');
      }

      // Força recriação
      await database;
      print('Novo banco criado com sucesso!');
    } catch (e) {
      print('Erro ao resetar DB: $e');
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