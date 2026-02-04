import '../models/RegionCategory.dart';

class AppConstants {
  static List<RegionCategory> regions = [
    RegionCategory(
        name: "All Areas",
        imagePath: "assets/images/regions/all_areas.png",
        databaseValue: "all_areas"),
    RegionCategory(
        name: "Moss Grotto",
        imagePath: "assets/images/regions/moss_grotto.png",
        databaseValue: "Moss Grotto"),
    RegionCategory(
        name: "The Marrow",
        imagePath: "assets/images/regions/the_marrow.png",
        databaseValue: "the_marrow"),
    RegionCategory(
        name: "Deep Docks",
        imagePath: "assets/images/regions/deep_docks.png",
        databaseValue: "deep_docks"),
    RegionCategory(
        name: "The Citadel",
        imagePath: "assets/images/regions/the_citadel.png",
        databaseValue: "the_citadel"),
    RegionCategory(
        name: "Greymoor",
        imagePath: "assets/images/regions/greymoor.png",
        databaseValue: "greymoor")
  ];
}