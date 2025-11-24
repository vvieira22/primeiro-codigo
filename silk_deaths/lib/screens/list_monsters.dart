import 'package:flutter/material.dart';

import '../models/Monster.dart';
import '../theme/app_colors.dart';

const String rightArrow = 'assets/images/arrow_right.png';
const String leftArrow = 'assets/images/arrow_left.png';

class ListItemCard extends StatelessWidget {
  final Monster monster;

  const ListItemCard({
    Key? key,
    required this.monster
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      color: AppColors.listMonstersBackgroundColor,
      shape: RoundedRectangleBorder(
        side: const BorderSide(
          color: AppColors.listMonstersBorderColor,
          width: 3.0,
        ),
        borderRadius: BorderRadius.circular(40.0),
      ),
      margin: EdgeInsets.zero, // Adicionado para garantir que não há margem externa na Card
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Column(
            children: [
              SizedBox(
                width: 100, //largura
                height: 120, //altura
                child: Stack(
                  alignment: Alignment.center,
                  children: [
                    // Moldura
                    Image.asset(
                      'assets/images/rounded_img_monsters.png',
                      fit: BoxFit.fill,
                      width: 100,
                      height: 120,
                    ),
                    // Imagem do boss
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: ClipOval(
                        child: Image.asset(monster.bossImageUrl, fit: BoxFit.fill),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),

          // Espaço lateral entre imagem e texto
          const SizedBox(width: 6),

          // === TEXTO ===
           Expanded(
              child: Padding(
                padding: const EdgeInsets.symmetric(vertical: 4.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(
                      monster.name,
                      style: const TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 24,
                      ),
                    ),
                    Text(
                    monster.boss ? "Boss" : "Enemy",
                      style: const TextStyle(fontSize: 20, color: Colors.grey),
                    ),
                    Text(
                      monster.regions.first,
                      style: const TextStyle(fontSize: 18, color: Colors.red),
                      maxLines: 2,
                      overflow: TextOverflow.ellipsis,
                    ),
                    Text(
                      "Mandatory",
                      style: const TextStyle(fontSize: 18, color: Colors.white),
                    ),
                  ],
                ),
              ),
            ),

          // --- WIDGET DO CONTADOR ---
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Image.asset(
                  leftArrow,
                  width: 30,
                  height: 65),
              // const SizedBox(width: 4),
              Container(
                decoration: BoxDecoration(
                  color: Colors.black,
                  borderRadius: BorderRadius.circular(8.0),
                ),
                child: SizedBox(
                  width: 80, // Largura fixa para o contador
                  child: Text(
                    "99999",
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 26,
                      fontWeight: FontWeight.bold,
                    ),
                    textAlign: TextAlign.center,
                  ),
                ),
              ),
              const SizedBox(width: 1),
              Image.asset(
                  rightArrow,
                  width: 30,
                  height: 65),
            ],
          ),

          // === SETA ===
          // Icon(Icons.arrow_forward_ios, size: 32, color: Colors.grey),
        ],
      ),
    );
  }
}
