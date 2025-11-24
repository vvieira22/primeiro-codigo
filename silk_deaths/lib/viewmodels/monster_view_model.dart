import 'package:flutter/material.dart';
import '../enums/ui_data_status.dart';
import '../services/auth/auth_local.dart';
import '../models/Monster.dart';

class MonsterViewModel extends ChangeNotifier {
  final AuthLocal _authLocal = AuthLocal();

  List<Monster> _monsters = [];
  UiDataStatus _status = UiDataStatus.initial;

  List<Monster> get monsters => _monsters;
  UiDataStatus get status => _status;

  MonsterViewModel() {
    fetchMonsters();
  }

  Future<void> fetchMonsters() async {
    _status = UiDataStatus.loading;
    notifyListeners();

    try {
      _monsters = await _authLocal.getMonsters();
      _status = UiDataStatus.loaded;
    } catch (e) {
      print('Erro no ViewModel ao buscar: $e');
      _status = UiDataStatus.error;
      _monsters = [];
    }

    notifyListeners();
  }
}
