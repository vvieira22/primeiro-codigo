extension StringExtensions on String {
  String capitalizeFirst() {
    if (isEmpty) {
      return this;
    }
    return "${this[0].toUpperCase()}${substring(1)}";
  }

  String clearAndUpperName() =>
      split("_").join(" ").capitalizeFirst();
}