import 'package:flutter/material.dart';

class HomeDrawer2 extends StatefulWidget {
  const HomeDrawer2({super.key});

  @override
  State<HomeDrawer2> createState() => _HomeDrawer2State();
}

class _HomeDrawer2State extends State<HomeDrawer2> {
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
        image: DecorationImage(
          image: AssetImage('assets/images/wallpapers/wallpaper6.png'),
          fit: BoxFit.cover,
        ),
      ),
      child: Padding(
        padding: const EdgeInsets.only(top: 50, left: 20, bottom: 70),
        child: Column(
          children: <Widget> [
            Row(
              children: <Widget> [
                // CircleAvatar(
                //   backgroundColor: Colors.blue,
                //   child: ClipRRect(
                //     borderRadius : BorderRadius.circular(20),
                //     child: Image(
                //       fit: BoxFit.cover,
                //       image: AssetImage('assets/images/wallpaper.png'),
                //     )
                //   ),
                // ),

                Text(
                  'Silk Deaths',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 40,
                    fontWeight: FontWeight.bold,
                    shadows: [
                      Shadow(
                        blurRadius: 30.0,
                        color: Colors.black,
                        offset: Offset(15.0, 5.0),
                      ),
                    ],
                  ),
                ),
              ]
            ),
            Column(
              children: <Widget> [
                SizedBox(
                  height: 100,
                ),
                NewRow(text: "Meu perfil",
                    icon: Icons.person),
                SizedBox(
                  height: 10,
                ),
                NewRow(
                    text: "Configurações",
                    icon: Icons.settings),
                SizedBox(
                  height: 10,
                ),
                NewRow(
                    text: "Sobre o App",
                    icon: Icons.info),
                SizedBox(
                  height: 10,
                ),
                NewRow(
                    text: "Sair",
                    icon: Icons.exit_to_app),
                SizedBox(
                  height: 10,
                ),
                // Row(
                //   children: <Widget> [
                //     Icon(
                //       Icons.copyright,
                //       color: Colors.white,
                //       size: 30,
                //     ),
                //     SizedBox(
                //         width : 10
                //     ),
                //     Text(
                //       "Teste",
                //       style: TextStyle(
                //         color: Colors.white,
                //         fontSize: 20,
                //         fontWeight: FontWeight.bold,
                //       ),
                //     )
                //   ]
                // )
              ]
            )
          ]
        ),
      )
    );
  }
}

class NewRow extends StatelessWidget {
  final String text;
  final IconData icon;

  const NewRow({
    super.key, required this.text, required this.icon
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      children: <Widget> [
        Icon(
          icon,
          color: Colors.white,
          size: 30,
            shadows: [
              Shadow(
                blurRadius: 30.0,
                color: Colors.black,
                offset: Offset(15.0, 5.0),
              ),
            ]
        ),
        SizedBox(width : 10),
        Text(
          text,
          style: TextStyle(
            color: Colors.white,
            fontSize: 25,
            fontWeight: FontWeight.bold,
              shadows: [
                Shadow(
                  blurRadius: 30.0,
                  color: Colors.black,
                  offset: Offset(15.0, 5.0),
                ),
              ]
          ),

        ),
      ]
    );
  }
}
