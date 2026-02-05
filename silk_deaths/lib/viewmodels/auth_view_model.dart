import 'package:flutter/cupertino.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

import '../enums/auth_status.dart';
import '../enums/ui_data_status.dart';
import '../services/auth/auth_local.dart';

class AuthViewModel extends ChangeNotifier {
  final FlutterSecureStorage _storage = const FlutterSecureStorage();
  final AuthLocal _authLocal = AuthLocal();
  UiDataStatus _status = UiDataStatus.uninitialized;

  UiDataStatus get status => _status;

  AuthViewModel() {
    _checkSession();
  }

  Future<void> _checkSession() async {
    String? token = await _storage.read(key: 'user_token');

    if (token != null) {
      _status = UiDataStatus.authenticated;
    } else {
      _status = UiDataStatus.unauthenticated;
    }
    notifyListeners();
  }

  Future<void> login(String email, String password) async {
    _status = UiDataStatus.authenticating;
    notifyListeners();
    final user = await _authLocal.login(email, password);
    if (user != null) {
      await _storage.write(key: 'user_token', value: 'token_da_api');

      _status = UiDataStatus.authenticated;
      notifyListeners();
    }
  }

  Future<void> logout() async {
    await _storage.delete(key: 'user_token');
    _status = UiDataStatus.unauthenticated;
    notifyListeners();
  }
}