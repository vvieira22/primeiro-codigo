class Monster {
  String name;
  String region;
  int deaths;
  bool boss = false;
  bool optional = false;
  late String bossImageUrl = defineBossImageUrl();

  Monster({
    required this.name,
    required this.region,
    required this.deaths,
    required this.boss,
    required this.optional});

  String defineBossImageUrl(){
    final basePath = boss ? "assets/images/monsters/bosses" : "assets/images/monsters";
    return "$basePath/boss_${name.toLowerCase()}.png";
  }
}