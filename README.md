# Guia Rápido: Principais Funcionalidades do `dart`

## Estrutura Básica

```dart
void main() {
  print('Olá, Dart!');
}
```

## Tipos de Dados

- `int`, `double`, `String`, `bool`, `List`, `Map`, `Set`
- Inferência: `var`, `final`, `const`

## Variáveis

```dart
int idade = 30;
final nome = 'Vitor';
const pi = 3.14;
```
## Variáveis *Dynamic* vs *Var* vs *Num*
Dynamic são variáveis que podem receber qualquer tipo de dado após sua criação. Var, é definido e sempre precisará ser daquele tipo criado, e o tipo num só irá aceitar números, inteiros ou decimais.
```dart
dynamic variavelDynamic = "30";
var variavelVar = 30
num numero = 30

variavelDynamic = 30;
variavelVar = 30
numero = 3.0

variavelVar = "30" #Erro !!
numero = "30" #Erro !!
```
## Funções

```dart
int soma(int a, int b) => a + b;
```

### Diferença entre parâmetros `{}` e `[]` em funções
Resumindo, posicionais sempre obrigatória, já nomeadas só quando coloco required na frente. 

- Parâmetros entre `{}` são **nomeados** e podem ser passados em qualquer ordem. Podem ser opcionais e ter valor padrão.
- Parâmetros entre `[]` são **posicionais opcionais** e devem ser passados na ordem definida.

```dart
void exemplo({int? x, int y = 2}) {
  print('$x $y');
}

void exemplo2([int? x, int y = 2]) {
  print('$x $y');
}
```

### Parâmetro `required`

- O modificador `required` é usado para tornar um parâmetro nomeado obrigatório.

```dart
void mostrarMensagem({required String mensagem}) {
  print(mensagem);
}
```

## Classes e Objetos

```dart
class Pessoa {
  String nome;
  Pessoa(this.nome);
}
var p = Pessoa('Vitor');
```

## Herança e Interfaces

```dart
class Animal {}
class Cachorro extends Animal {}
```

## Coleções

```dart
List<int> numeros = [1, 2, 3];
Map<String, int> mapa = {'a': 1, 'b': 2};
Set<int> conjunto = {1, 2, 3};
```

## Controle de Fluxo

```dart
if (true) {}
for (var i = 0; i < 5; i++) {}
while (condicao) {}
switch (valor) {}
```

## Operação Ternária

A operação ternária permite fazer decisões simples em uma linha:

```dart
var resultado = condicao ? valorSeVerdadeiro : valorSeFalso;
```

Exemplo:

```dart
int idade = 18;
String status = idade >= 18 ? 'Adulto' : 'Menor';
```

## Null Safety

```dart
String? nome; // pode ser nulo
```

## Null-aware Operators (`??`, `??=`, `?.`)

Null-aware operators ajudam a lidar com valores que podem ser nulos:

- `??`: Retorna o valor à esquerda se não for nulo, senão retorna o valor à direita.
- `??=`: Atribui um valor à variável apenas se ela for nula.
- `?.`: Permite acessar membros ou métodos de um objeto apenas se ele não for nulo.

Exemplos:

```dart
String? nome;
String resultado = nome ?? 'Desconhecido'; // Se nome for nulo, resultado será 'Desconhecido'

int? idade;
idade ??= 18; // Se idade for nulo, recebe 18

Pessoa? pessoa;
print(pessoa?.nome); // Só acessa 'nome' se pessoa não for nulo
```

Esses operadores ajudam a evitar erros de acesso a variáveis nulas e garantem maior segurança no código.

## Async/Await

```dart
Future<void> main() async {
  await Future.delayed(Duration(seconds: 1));
}
```

## Imports

```dart
import 'dart:math';
```

## Outros Recursos

- Mixins: `with`
- Extensions
- Generics: `<T>`
- Operadores: `??`, `?.`, `!`

## Ferramentas

- `dart run`
- `dart format`
- `dart analyze`

---

> Para detalhes, consulte a [documentação oficial](https://dart.dev/guides).