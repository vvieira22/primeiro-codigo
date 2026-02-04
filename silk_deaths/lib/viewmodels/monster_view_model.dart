import 'package:flutter/material.dart';
import '../const/app_const.dart';
import '../enums/ui_data_status.dart';
import '../models/RegionCategory.dart';
import '../services/auth/auth_local.dart';
import '../models/Monster.dart';

class MonsterViewModel extends ChangeNotifier {
  final AuthLocal _authLocal = AuthLocal();
  String _selectedRegion = "";

  List<Monster> _monsters = [];
  UiDataStatus _status = UiDataStatus.initial;

  final List<RegionCategory> categories = AppConstants.regions;

  // List<Monster> get monsters => _monsters;
  List<Monster> get monsters {

    if (_selectedRegion.isEmpty) {
      return _monsters;
    }

    return _monsters.where((m) {
      bool matches = m.databaseRegionsName.contains(_selectedRegion);
      // print('Procurando por: "$_selectedRegion"');
      // print('No Monstro: ${m.name}');
      // print('Regiões do Monstro: ${m.databaseRegionsName}');
      // print('Resultado: $matches');
      return matches;
    }).toList();
  }
  UiDataStatus get status => _status;

  MonsterViewModel() {
    fetchMonsters();
  }

  setRegion(String region) async{
    _status = UiDataStatus.loading;
    notifyListeners();
    await Future.delayed(const Duration(milliseconds: 300));

    _selectedRegion = region;
    _status = UiDataStatus.loaded;
    notifyListeners();
  }

  Future<void> fetchMonsters() async {
    _status = UiDataStatus.loading;
    notifyListeners();

    try {
      _monsters = await _authLocal.getMonsters();
      List<Monster> processedMonsters = [];
      for (var monster in _monsters) {
        if (monster.regions.length > 1) {
          for (int i = 0; i < monster.regions.length; i++) {
            processedMonsters.add(Monster(
              id: monster.id,
              name: monster.name,
              regions: [monster.regions[i]],
              databaseRegionsName: [monster.databaseRegionsName[i]],
              deaths: monster.deaths,
              boss: monster.boss,
              optional: monster.optional,
              act: monster.act,
            ));
          }
        } else {
          processedMonsters.add(monster);
        }
      }
      _monsters = processedMonsters;
      _status = UiDataStatus.loaded;
    } catch (e) {
      print('Erro no ViewModel ao buscar: $e');
      _status = UiDataStatus.error;
      _monsters = [];
    }

    notifyListeners();
  }

  Future<void> updateMonster(Monster monster) async {
    try {
      await _authLocal.updateMonster(monster);
      notifyListeners();
    }catch (e) {
      print('Erro no ViewModel ao atualizar: $e');
      _status = UiDataStatus.error;
      _monsters = [];
    }
  }
}
