import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:silk_deaths/viewmodels/auth_view_model.dart';
import 'package:url_launcher/url_launcher.dart';

import '../viewmodels/monster_view_model.dart';

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
      child: Consumer<AuthViewModel>(
          builder: (context, viewModel, child) {
            return Padding(
              padding: const EdgeInsets.only(top: 50, left: 20, bottom: 70),
              child: Column(
                  children: <Widget>[
                    Row(
                        children: <Widget>[
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
                        children: <Widget>[
                          SizedBox(
                            height: 100,
                          ),
                          GestureDetector(
                            onTap: () {
                              showDialog(
                                context: context,
                                builder: (context) => AlertDialog(
                                  title: const Text("About The App"),
                                  content: Column(
                                    mainAxisSize: MainAxisSize.min,
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                      const Text(
                                        "Silk Deaths is a free app, built and designed to practice Flutter.\n\n"
                                        "Feel free to reach out with questions or suggestions!.",
                                      ),
                                      const SizedBox(height: 20),
                                      RichText(
                                        text: TextSpan(
                                          style: const TextStyle(color: Colors.black, fontSize: 16),
                                          children: [
                                            const TextSpan(text: "Launcher/Loading Logo: "),
                                            TextSpan(
                                              text: "u/dotvhs",
                                              style: const TextStyle(
                                                color: Colors.blue,
                                                decoration: TextDecoration.underline,
                                              ),
                                              recognizer: TapGestureRecognizer()
                                                ..onTap = () async {
                                                  final url = Uri.parse('https://www.reddit.com/r/macgaming/comments/1nbgnhh/i_wasnt_very_happy_with_silksongs_icon_on_macos/');
                                                  if (await canLaunchUrl(url)) {
                                                    await launchUrl(url, mode: LaunchMode.externalApplication);
                                                  }
                                                },
                                            ),
                                          ],
                                        ),
                                      ),
                                      RichText(
                                        text: TextSpan(
                                          style: const TextStyle(color: Colors.black, fontSize: 16),
                                          children: [
                                            const TextSpan(text: "Original Repository: "),
                                            TextSpan(
                                              text: "github.com",
                                              style: const TextStyle(
                                                color: Colors.blue,
                                                decoration: TextDecoration.underline,
                                              ),
                                              recognizer: TapGestureRecognizer()
                                                ..onTap = () async {
                                                  final url = Uri.parse('https://github.com/vvieira22/primeiro-codigo/tree/flutter/silk_deaths/');
                                                  if (await canLaunchUrl(url)) {
                                                    await launchUrl(url, mode: LaunchMode.externalApplication);
                                                  }
                                                },
                                            ),
                                          ],
                                        ),
                                      ),
                                      RichText(
                                        text: TextSpan(
                                          style: const TextStyle(color: Colors.black, fontSize: 16),
                                          children: [
                                            const TextSpan(text: "Contact-me: "),
                                            TextSpan(
                                              text: "email",
                                              style: const TextStyle(
                                                color: Colors.blue,
                                                decoration: TextDecoration.underline,
                                              ),
                                              recognizer: TapGestureRecognizer()
                                                ..onTap = () async {
                                                  final url = Uri.parse('mailto:vitorgoncalvesvieira22@gmail.com?subject=Silk Deaths App');
                                                  if (await canLaunchUrl(url)) {
                                                    await launchUrl(url, mode: LaunchMode.externalApplication);
                                                  }
                                                },
                                            ),
                                          ],
                                        ),
                                      ),
                                    ],
                                  ),
                                  actions: [
                                    TextButton(
                                      onPressed: () => Navigator.pop(context),
                                      child: const Text("Fechar"),
                                    ),
                                  ],
                                ),
                              );
                            },
                            child: const NewRow(
                                text: "About",
                                icon: Icons.info),
                          ),
                          SizedBox(
                            height: 10,
                          ),
                          GestureDetector(
                            onTap: () {
                              context.read<AuthViewModel>().logout();
                            },
                            child: NewRow(
                                text: "Logout",
                                icon: Icons.exit_to_app),
                          ),
                          SizedBox(
                            height: 10,
                          ),
                        ]
                    )
                  ]
              ),
            );
          }
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
