import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:audioplayers/audioplayers.dart';
import 'dart:math';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter_staggered_animations/flutter_staggered_animations.dart';
import 'package:provider/provider.dart';
import 'package:silk_deaths/screens/home_screen.dart';
import 'package:silk_deaths/screens/home_screen2.dart';
import 'package:silk_deaths/screens/list_monsters.dart';
import 'package:silk_deaths/screens/login_screen.dart';
import 'package:silk_deaths/screens/register_screen.dart';
import 'package:silk_deaths/viewmodels/auth_view_model.dart';
import 'package:silk_deaths/viewmodels/monster_view_model.dart';
import 'package:silk_deaths/widgets/home_carousel.dart';
import 'package:silk_deaths/widgets/home_drawer.dart';
import 'package:silk_deaths/widgets/home_drawer2.dart';
import 'enums/ui_data_status.dart';
import 'firebase_options.dart';
import 'models/Monster.dart';

final db = FirebaseFirestore.instance;

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => MonsterViewModel()),
        ChangeNotifierProvider(create: (_) => AuthViewModel()),
      ],
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "SilkDeaths",
        theme: ThemeData(
          primarySwatch: Colors.blue,
          useMaterial3: true,
          textSelectionTheme: const TextSelectionThemeData(
            cursorColor: Colors.white, // Define a cor do cursor para o app todo
            selectionColor: Colors.white,
            selectionHandleColor: Colors.white,
          ),
        ),
        home: Consumer<AuthViewModel>(
          builder: (context, auth, _) {
            // Verificamos o status que você definiu na ViewModel
            switch (auth.status) {
              // case UiDataStatus.loading:
              //   return const SplashScreen(); // Uma tela simples com seu loading centralizado
              case UiDataStatus.authenticated:
                return HomeScreenLayout(); // Tela principal com monstros
              case UiDataStatus.unauthenticated:
              default:
                return const LoginScreen(); // Tela de login/cadastro
            }
          },
        ),
    );
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
      late final teste = <String,String> {
        "teste": "teste_$mortes",
        "teste2": "123"
      };
      db.collection("teste_$mortes")
          .doc("teste").set(teste)
          .onError((error, stacktrace) =>
          print("Erro firebase"));
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

class RoteadorTelas extends StatelessWidget {
  const RoteadorTelas({super.key});

  @override
  Widget build(BuildContext context) {
    return StreamBuilder(
        stream: FirebaseAuth.instance.userChanges(),
        builder: (context, snapshot){
          if(snapshot.connectionState == ConnectionState.waiting) {
            return const Center(
              child: CircularProgressIndicator(),
            );
          } else {
            if (snapshot.hasData) {
              return HomeScreen(user: snapshot.data!);
            } else {
              return LoginScreen();
            }}
        });
  }
}

class InfiniteListScreen extends StatefulWidget {
  InfiniteListScreen({Key? key}) : super(key: key);

  @override
  State<InfiniteListScreen> createState() => _InfiniteListScreenState();
}

class _InfiniteListScreenState extends State<InfiniteListScreen> {
  final PageController _pageController = PageController();
  int _currentIndex = 0;

  // Simula o número total de itens para o design - será movido para dentro do estado
  final int totalItems = 50;

  final List<String> imagesIdle = [
    'assets/images/regions/all_areas.png',
    'assets/images/regions/moss_grotto.png',
    'assets/images/regions/the_marrow.png',
    'assets/images/regions/deep_docks.png',
    'assets/images/regions/the_citadel.png',
    'assets/images/regions/greymoor.png',
  ];

  void _onCarouselPageChanged(int newIndex) {
    setState(() {_currentIndex = newIndex;});

    if(_currentIndex == 0){context.read<MonsterViewModel>().setRegion('');}
    if(_currentIndex == 1){context.read<MonsterViewModel>().setRegion('moss_grotto');}
    if(_currentIndex == 2){context.read<MonsterViewModel>().setRegion('the_marrow');}
    if(_currentIndex == 3){context.read<MonsterViewModel>().setRegion('deep_docks');}
    if(_currentIndex == 4){context.read<MonsterViewModel>().setRegion('the_citadel');}
    if(_currentIndex == 5){context.read<MonsterViewModel>().setRegion('greymoor');}
  }

   Color fadeColor = Colors.transparent;
   double fadeAmount = 0.1;

   double xOffset = 0;
   double yOffset = 0;
   bool isDrawerOpen = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: isDrawerOpen ? () {
        setState(() {
          xOffset = 0;
          yOffset = 0;
          isDrawerOpen = false;
        });
      } : null,
      child: AnimatedContainer(
        transform: Matrix4.translationValues(xOffset, yOffset, 0)
          ..scale(isDrawerOpen ? 0.85 : 1.00)
          ..rotateZ(isDrawerOpen ? -50: 0), // A rotação pode ser um pouco demais
        duration: Duration(milliseconds: 250),
        decoration: BoxDecoration( // Adicionado para evitar problemas de renderização durante a animação
          color: Colors.black,
          borderRadius: BorderRadius.circular(isDrawerOpen ? 40 : 0.0),
        ),
        child: Scaffold(
          backgroundColor: Colors.black,
          extendBodyBehindAppBar: true,
          appBar: AppBar(
              iconTheme: const IconThemeData(
                color: Colors.red, // Set your desired color here
              ),
            title: const Text('Silk Deaths'),
            titleTextStyle: const TextStyle(
              color: Colors.white,
              fontSize: 30,
              fontWeight: FontWeight.bold,
            ),
            backgroundColor: Colors.transparent,
            elevation: 0,
            leading: IconButton( // Adiciona um botão para abrir/fechar o drawer
              icon: Icon(isDrawerOpen ? Icons.arrow_back_ios : Icons.menu),
              onPressed: () {
                setState(() {
                  if (isDrawerOpen) {
                    xOffset = 0;
                    yOffset = 0;
                    isDrawerOpen = false;
                  } else {
                    xOffset = 300;
                    yOffset = 50;
                    isDrawerOpen = true;
                  }
                });
              },
            ),
          ),
          // O segredo está aqui: o Stack permite sobrepor o loading sem remover o fundo
          body: Stack(
            children: [
              // CAMADA 1: O CONTEÚDO (Sempre fixo no fundo)
              Column(
                children: [
                  const SizedBox(height: 80),
                  HomeCarousel(
                    images: imagesIdle,
                    onPageChanged: _onCarouselPageChanged,
                  ),
                  Expanded(
                    child: AnimationLimiter(
                      child: ShaderMask(
                        shaderCallback: (Rect rect) {
                          return const LinearGradient(
                            begin: Alignment.topCenter,
                            end: Alignment.bottomCenter,
                            colors: [Colors.transparent, Colors.black, Colors.black, Colors.transparent],
                            stops: [0.0, 0.05, 0.95, 1.0],
                          ).createShader(rect);
                        },
                        blendMode: BlendMode.dstIn,
                        child: Consumer<MonsterViewModel>(
                          builder: (context, viewModel, child) {
                            // Se a lista estiver vazia mas não estiver carregando, mostra um aviso
                            if (viewModel.monsters.isEmpty && viewModel.status == UiDataStatus.loaded) {
                              return const Center(child: Text("No monsters found", style: TextStyle(color: Colors.white)));
                            }

                            return ListView.builder(
                              itemCount: viewModel.monsters.length,
                              padding: const EdgeInsets.only(top: 5, bottom: 30),
                              itemBuilder: (context, index) {
                                final Monster monstroReal = viewModel.monsters[index];
                                return AnimationConfiguration.staggeredList(
                                  position: index,
                                  duration: const Duration(milliseconds: 800),
                                  child: SlideAnimation(
                                    verticalOffset: 100.0,
                                    child: FadeInAnimation(child: ListItemCard(monster: monstroReal)),
                                  ),
                                );
                              },
                            );
                          },
                        ),
                      ),
                    ),
                  ),
                ],
              ),

              // CAMADA 2: O LOADING TRANSPARENTE (Fica por cima de tudo)
              Consumer<MonsterViewModel>(
                builder: (context, viewModel, child) {
                  // Se não estiver carregando, retorna um widget vazio (não desenha nada)
                  if (viewModel.status != UiDataStatus.loading) {
                    return const SizedBox.shrink();
                  }

                  return Container(
                    color: Colors.black.withValues(alpha: 0.7), // Levíssimo escurecimento
                    child: Center(
                      child: SizedBox(
                        width: 160,
                        height: 160,
                        child: Image.asset('assets/icons/icon_launcher.png'), // Seu ícone centralizado
                      ),
                    ),
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class HomeScreenLayout extends StatefulWidget {
  const HomeScreenLayout({super.key});

  @override
  State<HomeScreenLayout> createState() => _HomeScreenLayoutState();
}

class _HomeScreenLayoutState extends State<HomeScreenLayout> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Stack(
          children: [
            HomeDrawer2(), // Coloca o conteúdo do drawer por trás
            InfiniteListScreen(),
          ],
        ),
      )
    );
  }
}
