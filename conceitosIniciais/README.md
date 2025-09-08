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

# Métodos Avançados para Listas em Dart

### `List.filled()`

Cria uma lista de tamanho fixo onde todos os elementos são preenchidos com o mesmo valor.

```dart
// Cria uma lista com 10 posições, todas preenchidas com a string "Vitor"
List<String> nomes = List.filled(10, "Vitor");
print(nomes); // [Vitor, Vitor, Vitor, Vitor, Vitor, Vitor, Vitor, Vitor, Vitor, Vitor]
```

### `List.generate()`

Cria uma lista cujo conteúdo é gerado por uma função. A função recebe o índice do elemento como parâmetro e deve retornar o valor para aquela posição.

```dart
// Gera uma lista de 10 elementos, onde cada elemento é o seu índice multiplicado por 2.
List<int> lista = List.generate(10, (index) {
  return index * 2;
});
print(lista); // [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

// Versão simplificada com arrow function (=>)
List<int> lista2 = List.generate(10, (index) => (index + 1));
print(lista2); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

### `isEmpty` e `isNotEmpty`

Verificam de forma rápida e legível se a lista contém ou não elementos.

```dart
print(lista2.isEmpty);   // false
print(lista2.isNotEmpty); // true
```

### `any()`

Retorna `true` se **pelo menos um** elemento da lista satisfizer a condição da função.

```dart
// Verifica se existe algum elemento maior que 5 na lista.
bool temMaiorQue5 = lista2.any((elemento) => elemento > 5);
print(temMaiorQue5); // true
```

---

### `firstWhere()` e `lastWhere()`

- `firstWhere`: Retorna o **primeiro** elemento que atende à condição.
- `lastWhere`: Retorna o **último** elemento que atende à condição.

**Atenção:** Se nenhum elemento for encontrado, uma exceção (erro) será lançada.

```dart
// Retorna o primeiro número par da lista.
print(lista2.firstWhere((i) => i % 2 == 0)); // 2

// Retorna o último número par da lista.
print(lista2.lastWhere((i) => i % 2 == 0)); // 10
```

### `where()`

Retorna uma nova coleção **iterável** (`Iterable`) com **todos** os elementos que atendem à condição. Por não ser uma `List`, se você precisar dos métodos de lista (como `[]` ou `.length`), você deve convertê-la com `.toList()`.

```dart
// Retorna um Iterable com todos os números pares.
var numerosPares = lista2.where((i) => i % 2 == 0);
print(numerosPares); // (2, 4, 6, 8, 10)

// Para usar como lista, converta:
List<int> listaDePares = numerosPares.toList();
print(listaDePares[0]); // 2
```

---

### `map()`

Aplica uma função a **cada elemento** da lista e retorna um novo `Iterable` com os resultados. É a ferramenta perfeita para transformar dados.

```dart
// Cria um novo Iterable onde cada elemento da lista original foi incrementado em 1.
var listaIncrementada = lista2.map((i) => i + 1);
print(listaIncrementada.toList()); // [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

// Você também pode usar uma função com lógica mais complexa.
var resultadoComplexo = lista2.map((i) => i % 2 == 0 ? i * 10 : i);
print(resultadoComplexo.toList()); // [1, 20, 3, 40, 5, 60, 7, 80, 9, 100]
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

### Esses operadores ajudam a evitar erros de acesso a variáveis nulas e garantem maior segurança no código.

```dart
Map<String, dynamic> usuario = {
  'nome': 'Alice',
  'idade': 30,
  'ativo': true,
};
print(usuario); // {nome: Alice, idade: 30, ativo: true}

// Map vazio
Map<String, int> idades = {};
```

Acesse usando a chave entre colchetes `[]`.

```dart
print(usuario['nome']);   // Alice
print(usuario['idade']);  // 30

// Se a chave não existir, retorna null
print(usuario['email']); // null
```

### Adicionando/Atualizando Valores

Use a chave entre colchetes `[]` e atribua um valor.

```dart
usuario['cidade'] = 'São Paulo'; // Adiciona uma nova chave/valor
usuario['idade'] = 31;         // Atualiza o valor da chave 'idade'
print(usuario); // {nome: Alice, idade: 31, ativo: true, cidade: São Paulo}
```

### Removendo Valores

Use o método `remove()`.

```dart
usuario.remove('ativo');
print(usuario); // {nome: Alice, idade: 31, cidade: São Paulo}
```

### Verificando Chaves e Valores

- `containsKey()`: Verifica se a chave existe.
- `containsValue()`: Verifica se o valor existe.
- `isEmpty`, `isNotEmpty`: Verificam se o map está vazio.
- `length`: Retorna o número de pares chave/valor.

```dart
print(usuario.containsKey('nome'));  // true
print(usuario.containsKey('email')); // false
print(usuario.containsValue('Alice')); // true
print(usuario.isEmpty);             // false
print(usuario.length);              // 3
```

### Iterando sobre um Map

Use `forEach()` ou um loop `for-in` nos métodos `keys`, `values` ou `entries`.

```dart
// Iterando com forEach
usuario.forEach((chave, valor) {
  print('$chave: $valor');
});
// Saída:
// nome: Alice
// idade: 31
// cidade: São Paulo

// Iterando sobre as chaves
for (var chave in usuario.keys) {
  print('Chave: $chave');
}

// Iterando sobre os valores
for (var valor in usuario.values) {
  print('Valor: $valor');
}

// Iterando sobre pares chave/valor (entries)
for (var entry in usuario.entries) {
  print('Chave: ${entry.key}, Valor: ${entry.value}');
}
```

### Outros Métodos Úteis

- `clear()`: Remove todos os pares chave/valor.
- `putIfAbsent()`: Adiciona um par chave/valor apenas se a chave ainda não existir.
- `update()`: Atualiza o valor de uma chave existente.
- `map()`: Cria um novo map aplicando uma função a cada entrada.

```dart
Map<String, int> contadores = {'a': 1, 'b': 2};

// Adiciona 'c': 3 apenas se 'c' não existir
contadores.putIfAbsent('c', () => 3);
print(contadores); // {a: 1, b: 2, c: 3}

// Não adiciona 'a' porque já existe
contadores.putIfAbsent('a', () => 10);
print(contadores); // {a: 1, b: 2, c: 3}

// Atualiza o valor de 'a'
contadores.update('a', (valorAtual) => valorAtual * 2);
print(contadores); // {a: 2, b: 2, c: 3}

// Cria um novo map com valores dobrados
var contadoresDobrados = contadores.map((key, value) => MapEntry(key, value * 2));
print(contadoresDobrados); // {a: 4, b: 4, c: 6}


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