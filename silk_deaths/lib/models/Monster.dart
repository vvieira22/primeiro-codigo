import 'package:silk_deaths/extensions/string_extensions.dart';

class Monster {
  int? id;
  String name;
  List<String> regions;
  int deaths;
  bool boss = false;
  bool optional = false;
  int act;
  late String bossImageUrl = defineBossImageUrl();

  Monster({
    this.id,
    required this.name,
    required this.regions,
    required this.deaths,
    required this.boss,
    required this.optional,
    required this.act
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name': name.clearAndUpperName(),
      'regions': regions.join('|'),
      'deaths': deaths,
      'boss': boss ? 1 : 0,
      'optional': optional ? 1 : 0,
      'act': act,
    };
  }

  factory Monster.fromJson(Map<String, dynamic> map) {
    return Monster(
      name: map['name'],
      regions: List<String>.from(map['regions'] ?? []),
      deaths: map['deaths'] ?? 0,
      boss: map['boss'] == 1 || map['boss'] == true,
      optional: map['optional'] == 1 || map['optional'] == true,
      act: map['act'] ?? 0,
    );
  }

  factory Monster.fromMap(Map<String, dynamic> map) {

    String regionsString = map['regions'] as String;
    List<String> regionsList = regionsString.isNotEmpty
        ? regionsString.split('|').map((region) => region.clearAndUpperName()).toList()
        : [];

    return Monster(
      id: map['id'] as int?,
      name: map['name'] as String,
      regions: regionsList,
      deaths: map['deaths'] as int,
      boss: map['boss'] == 1,
      optional: map['optional'] == 1,
      act: map['act'] as int,
    );
  }

  String defineBossImageUrl() {
    final basePath = boss ? "assets/images/monsters/bosses" : "assets/images/monsters/common";
    return "$basePath/${name.toLowerCase().replaceAll(' ', '_')}.png";
  }
}