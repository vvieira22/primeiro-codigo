import 'package:flutter/material.dart';
import 'package:smooth_page_indicator/smooth_page_indicator.dart';
typedef PageChangedCallback = void Function(int newIndex);

class HomeCarousel extends StatefulWidget {

  final List<String> images;
  final PageChangedCallback? onPageChanged;

  const HomeCarousel({
    super.key,
    required this.images,
    this.onPageChanged,
  });

  @override
  State<HomeCarousel> createState() => _HomeCarouselState();
}

class _HomeCarouselState extends State<HomeCarousel> {
  late PageController _pageController;
  final double _viewportFraction = 1; // Ajuste para 85% do tamanho da página

  @override
  void initState() {
    super.initState();
    _pageController = PageController(
      initialPage: 0,
      viewportFraction: _viewportFraction,
    );
    _pageController.addListener(_handlePageChange);
  }

  // 4. Funcao de escuta
  void _handlePageChange() {
    // PageView.builder pode ter páginas parciais (ex: 0.5, 1.3),
    // então convertemos para o índice inteiro para saber qual é a página principal.
    final double? currentPageIndex = _pageController.page;

    if(currentPageIndex != null && currentPageIndex == currentPageIndex.roundToDouble()){
      // Verifica se houve uma mudança de índice inteiro (se a rolagem parou em uma nova página)
      // E garante que o callback foi fornecido
      if (widget.onPageChanged != null) {
        // 5. Chama a função que foi passada pelo pai (HomeScreen)
        widget.onPageChanged!(currentPageIndex.round());
      }
    }
  }

  @override
  void dispose() {
    _pageController.removeListener(_handlePageChange);
    _pageController.dispose();
    super.dispose();
  }

  Widget _buildCarouselItem(int index) {
    double scale = 1.0;

    // Lógica para calcular a escala baseada na posição do scroll
    if (_pageController.hasClients) {
      final double page = _pageController.page ?? 0.0;
      final double difference = (index - page).abs();

      const double maxScale = 0.9;
      // Garante que o scale está entre 0.9 e 1.0 (central)
      scale = (1.0 - difference * (1.0 - maxScale)).clamp(maxScale, 1.0);
    }

    return AnimatedBuilder(
      animation: _pageController,
      builder: (context, child) {
        return Transform.scale(
          scale: scale,
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 6.0),
            child: Container(
              margin: const EdgeInsets.symmetric(vertical: 16),
              decoration: BoxDecoration(
                // Use a cor de fundo do seu Container
                color: Colors.grey[800],
                borderRadius: BorderRadius.circular(32),
                image: DecorationImage(
                  // Acessa as imagens através do widget.images
                  image: AssetImage(widget.images[index]),
                  fit: BoxFit.cover,
                ),
                boxShadow: const [
                  BoxShadow(
                    color: Colors.black26,
                    blurRadius: 10,
                    offset: Offset(0, 5),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SizedBox(
          height: 250, // Altura fixa para o carrossel
          child: PageView.builder(
            controller: _pageController,
            itemCount: widget.images.length,
            itemBuilder: (context, index) {
              return _buildCarouselItem(index);
            },
          ),
        ),
        const SizedBox(height: 16),
        // Opcional: Indicador de Página (Se tiver o pacote smooth_page_indicator)

        SmoothPageIndicator(
          controller: _pageController,
          count: widget.images.length,
          effect: const JumpingDotEffect(
            dotHeight: 8,
            dotWidth: 8,
            activeDotColor: Colors.white,
          ),
        ),

      ],
    );
  }
}