import 'package:flutter/cupertino.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class LocaleProvider extends ChangeNotifier {
  final FlutterSecureStorage _storage = const FlutterSecureStorage();
  Locale _locale = const Locale('pt');

  Locale get locale => _locale;

  LocaleProvider() {
    _loadLocale(); // Carrega o idioma salvo assim que a ViewModel nasce
  }

  // Carrega do storage
  Future<void> _loadLocale() async {
    String? languageCode = await _storage.read(key: 'user_language');
    if (languageCode != null) {
      _locale = Locale(languageCode);
      notifyListeners();
    }
  }

  // Muda o idioma e salva para a próxima vez
  Future<void> setLocale(Locale locale) async {
    _locale = locale;
    await _storage.write(key: 'user_language', value: locale.languageCode);
    notifyListeners();
  }
}