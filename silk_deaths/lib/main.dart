import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:audioplayers/audioplayers.dart';
import 'dart:math';

//primeira funcao quando executa app.
void main() {
  // Garante que os bindings do Flutter sejam inicializados
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: HomePage());
  }
}

//StatefulWidget vs StatelessWidget, Basicamente o stateful muda o estado, o state fica pra sempre assim.
//dependendo é necessairo usar state para evitar dar refresh.
class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int mortes = 0;
  final AudioPlayer _audioPlayer = AudioPlayer();

  //Precisa colocar o setState por que é ele quem avisa o flutter que precisa reconstruir a tela com o novo valor da variável.
  void increment() {
    setState(() {
      mortes++;
      playSoundDeath();
    });
    print(mortes);
  }

  void resetar() {
    setState(() {
      mortes = 0;
      playSoundReset();
    });
    print(mortes);
  }

  Future<void> playSoundDeath() async {
    if (_audioPlayer.state == PlayerState.playing) {
      await _audioPlayer.stop();
    }
      String randomSound = (Random().nextInt(7) + 1).toString();
    await _audioPlayer.play(AssetSource('sounds/$randomSound.mp3'));
  }

  Future<void> playSoundReset() async {
    if (_audioPlayer.state == PlayerState.playing) {
      await _audioPlayer.stop();
    }
    await _audioPlayer.play(AssetSource('sounds/reset.mp3'));
  }

  bool get isToMuchDeads => mortes > 20;

  // Scaffold é um widget que implementa a estrutura básica de layout visual do Material Design.
  // Basicamente, é um widget padrão que você usará na maioria das suas telas.
  // Ele fornece APIs para exibir drawers, snack bars e bottom sheets.
  //-> dica, selecionar widgete e apertar CTRL + W PRA SELECIONAR ELE INTEIRO PRA RECORTAR.
  //OU AINDA MELHOR, CLICAR NO WIDGTE E DIGITAR ALT + ENTER E PROCURAR PR AMOVER ELE PRA ALGUM LUGAR.
  @override
  //remove a statusbar do app, mas mantem a do android
  Widget build(BuildContext context) {
    SystemChrome.setSystemUIOverlayStyle(const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent, // Torna a status bar transparente
      statusBarIconBrightness: Brightness.light, // Define os ícones da status bar como claros
    ));
    return Scaffold(
      extendBodyBehindAppBar: false, // Permite que o corpo da Scaffold se estenda atrás da AppBar
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage('assets/images/wallpaper.png'),
            fit: BoxFit.cover,
          ),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Mortes:',
              style: TextStyle(
                fontSize: 30,
                color: Colors.white,
                fontWeight: FontWeight.bold,
                letterSpacing: 1,
              ),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(32, 16, 32, 64),
              child: Text(
                '$mortes',
                style: const TextStyle(
                  fontSize: 100,
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.white,
                    foregroundColor: Colors.black,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(30),
                    ),
                    fixedSize: const Size(
                        160,
                        100),
                  ),
                  onPressed: resetar,
                  child: Text(
                    'Resetar',
                    style: TextStyle(
                      fontSize: 30,
                      color: Colors.black,
                      fontWeight: FontWeight.bold,
                      letterSpacing: 1,
                    ),
                  ),
                ),
                const SizedBox(width: 32),
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: isToMuchDeads ? Colors.red : Colors.white,
                    foregroundColor: Colors.black,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(30),
                    ),
                    //essa é a cor quando clicar no botao
                    fixedSize: const Size(
                      160,
                      100,
                    ), //interessante pra ter botao com tamanho igual e texto diferente !!,
                  ),
                  onPressed: increment,
                  //sem parentese, voce quer chamar ela quando clicar e nao chamar e preencher quando iniciar.
                  child: const Text(
                    'Morri',
                    style: TextStyle(
                      fontSize: 30,
                      color: Colors.black,
                      fontWeight: FontWeight.bold,
                      letterSpacing: 1,
                    ),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}