## Estrutura de Pastas e Arquivos Importantes em um Projeto Flutter:

*   **`lib`**: Pasta onde reside todo o código Dart da sua aplicação.
*   **`windows`, `ios`, `android`, etc.** : Pastas específicas para cada plataforma, contendo código e configurações nativas.
*   **`pubspec.yaml`**: Arquivo de configuração central do projeto. Nele você define:
    *   Nome do projeto.
    *   Descrição.
    *   `publish_to`: Onde o app será publicado (ex: 'none' para não publicar, ou o endereço de um repositório).
    *   Versão do aplicativo.
    *   Versão do SDK do Dart.
    *   Dependências (pacotes externos que seu app utiliza).
    *   Assets (arquivos que o app vai usar, como imagens, fontes, etc.).
    *   Configurações de fontes padrão.

**Importante:** Sempre que você alterar o arquivo `pubspec.yaml` (adicionando uma dependência, por exemplo), é necessário executar o comando `flutter pub get` no terminal ou clicar no botão que geralmente aparece no seu editor de código (semelhante ao "Sync Gradle" no Android Studio para projetos nativos Android). Isso garante que as novas dependências sejam baixadas e configuradas corretamente.

#### Flutter suporta hot reload, mexeu no código ele já atualiza na tela :)

## Modos de Compilação (Build Modes) no Flutter 
O Flutter oferece três modos de compilação, cada um otimizado para uma fase diferente do desenvolvimento:
Obs: Para jogar na playstore é recomendado buildar appbundle em vez de apk!
1.  **Debug Mode:**
    *   **Propósito:** Usado durante o desenvolvimento ativo.
    *   **Características:**
        *   **Hot Reload e Hot Restart:** Permite atualizações rápidas de código sem perder o estado da aplicação (Hot Reload) ou reiniciando completamente a aplicação (Hot Restart).
        *   **Assertions Habilitadas:** Verificações de tempo de execução (como `assert`) estão ativas para ajudar a identificar erros durante o desenvolvimento.
        *   **Debugging e Profiling:** Ferramentas de depuração e análise de performance estão disponíveis.
        *   **Não Otimizado:** O código não é otimizado para performance ou tamanho, resultando em apps maiores e potencialmente mais lentos.
        *   **Marca d'água "Debug":** Uma faixa "Debug" é exibida no canto superior direito da tela.
    *   **Como usar:** É o modo padrão ao executar `flutter run`.

2.  **Release Mode:**
    *   **Propósito:** Usado para criar a versão final do aplicativo que será distribuída aos usuários.
    *   **Características:**
        *   **Otimização Máxima:** O código é compilado para a melhor performance e menor tamanho possível (compilação AOT - Ahead-Of-Time).
        *   **Assertions Desabilitadas:** Todas as verificações de `assert` são ignoradas.
        *   **Debugging Limitado:** As ferramentas de debugging são desabilitadas ou limitadas.
        *   **Sem Marca d'água:** A faixa "Debug" é removida.
    *   **Como usar:** Execute `flutter run --release` para rodar ou `flutter build <platform> --release` (ex: `flutter build apk --release` ou `flutter build ipa --release`) para gerar o artefato de compilação.

3.  **Profile Mode:**
    *   **Propósito:** Usado para analisar a performance do aplicativo em um ambiente mais próximo do de produção, mas ainda permitindo algumas ferramentas de profiling.
    *   **Características:**
        *   **Compilação AOT (parcial):** Similar ao Release Mode em termos de compilação, mas mantém algumas funcionalidades para profiling.
        *   **Assertions Desabilitadas.**
        *   **Ferramentas de Profiling Disponíveis:** Permite o uso de ferramentas como o DevTools para analisar gargalos de performance, uso de memória, etc.
        *   **Sem Marca d'água "Debug".**
    *   **Como usar:** Execute `flutter run --profile` ou `flutter build <platform> --profile`. É útil para identificar problemas de performance antes de lançar a versão final.
**Em resumo:**
*   Use **Debug Mode** para o desenvolvimento diário.
*   Use **Profile Mode** para analisar a performance antes de lançar.
*   Use **Release Mode** para construir a versão final para os usuários.

## Widgets

Tudo em Flutter é construído a partir de widgets. Widgets são os blocos fundamentais da interface do usuário: cada elemento visual, como botões, textos, imagens, é um widget. Eles podem ser combinados e personalizados para criar as interfaces.

* StatefulWidget
É um widget que pode mudar com o tempo. Por exemplo, um botão que muda de cor quando você clica. Ele guarda informações (estado) e pode atualizar a tela quando algo muda.

* StatelessWidget
É um widget que nunca muda depois de criado. Ele só mostra informações fixas. Por exemplo, um texto ou um ícone que não muda.

* InheritedWidget
Serve para compartilhar informações entre vários widgets filhos. Por exemplo, se você quer que vários widgets tenham acesso ao mesmo tema ou configuração, usa um InheritedWidget para passar esses dados para baixo na árvore de widgets.

Se pensar em widgets como peças de LEGO:

**StatelessWidget** é uma peça fixa.
**StatefulWidget** é uma peça que pode mudar de cor ou forma.
**InheritedWidget** é como uma base que passa energia para várias peças conectadas.

### Scaffold

O Scaffold é um widget que implementa a estrutura visual básica do Material
Design. Pense nele como o "esqueleto" de uma tela. **Basicamente um dos widgets mais importantes, literalmente a base de tudo teoricamente**.

Por que usá-lo aqui?
* Estrutura Padrão: Ele fornece slots (propriedades) para os elementos mais comuns de uma tela, como `appBar` (barra superior), `body` (o conteúdo principal), `floatingActionButton` (botão de ação flutuante), `drawer` (menu lateral), `bottomNavigationBar` (barra de navegação inferior), etc.

* Aparência Consistente: Garante que sua tela siga as diretrizes do Material Design, como definir uma cor de fundo padrão (geralmente branco ou cinza claro) e garantir que o conteúdo não se sobreponha a elementos do sistema operacional (como a barra de status na parte superior ou a barra de gestos na parte inferior).

### Container
O Container é um widget versátil usado para layout, estilização e pintura. Você pode definir sua cor, tamanho, preenchimento (padding), margens, bordas e muito mais. É um dos blocos de construção mais fundamentaispara criar a UI (Interface de Usuário) final do seu aplicativo.

Exemplo: Um cabeçalho azul com altura definida.

### Placeholder
É um widget de desenvolvimento. Ele desenha uma caixa com um 'X' dentro para "reservar" um espaço na tela. É extremamente útil durante a fase de prototipagem e layout para visualizar onde os widgets futuros serão colocados sem precisar construí-los ainda.Ele não é destinado ao aplicativo final em produção.

Exemplo: Reservando espaço para um futuro formulário de login.

### Passagem parâmetros/widgets entre filhos/pai
1.  **Pai -> Filho:**
   Passagem por parâmetro simples.
2.  **Filho -> Pai:**
   Através de um callback (função), cria um callback no pai, passa pelo filho, então o filho recebe e "chama".

### BuildContext

Ele serve como um "endereço" que diz onde você está na árvore de widgets do app. Quando você cria um widget, o Flutter dá para ele um BuildContext.
Esse BuildContext permite que o widget encontre informações sobre onde ele está e acesse coisas como temas, tamanhos, ou navegar para outras telas.

BuildContext é só uma forma do Flutter saber "onde" você está no app, para poder te ajudar a acessar recursos ou navegar entre telas.