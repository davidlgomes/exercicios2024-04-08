# Exercícios do dia 2024-04-08

## Descrição

Este é um conjunto de funções e classes Python que realiza várias operações, como cálculos relacionados a consumo de carros, cálculos de valores de pagamentos em atraso, e manipulação de pontos e retângulos em um plano cartesiano.

## Funções Principais

### Lista21

- `calcularMinimoConsumo(carros, consumo)`: Calcula o carro mais econômico com base nos dados fornecidos de consumo.
- `exibirOrdemConsumo(carros, consumo)`: Exibe um relatório com os carros em ordem de consumo, do mais econômico ao menos econômico.

### Função 7

- `valorPagamento(prestacao, atraso)`: Calcula o valor a ser pago, considerando uma prestação base e os dias de atraso.
- `impressaoGeralValorPagamento()`: Realiza a impressão de valores de pagamento, permitindo ao usuário inserir várias prestações com seus respectivos atrasos.

### Classe 9

- `Ponto`: Representa um ponto em um plano cartesiano, com atributos `pontoX` e `pontoY`.
- `Retangulo`: Uma subclasse de `Ponto`, representa um retângulo com largura, altura e posição no plano cartesiano. Possui um método `centroRetangulo` para calcular o centro do retângulo.

#### MenuGeral

- `menuClasse()`: Permite ao usuário criar objetos do tipo `Ponto` e `Retangulo` e calcular o centro do último retângulo criado.
- `menuGeral()`: Um menu principal que permite ao usuário escolher entre as opções da Lista 21, Função 7 e Classe 9.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Baixe o arquivo `exerciciosUnificadoPythonBrasil.py`.
3. Abra um terminal e navegue até o diretório onde o arquivo foi baixado.
4. Execute o arquivo Python com o comando `python exerciciosUnificadoPythonBrasil.py`.
5. Siga as instruções apresentadas no console para interagir com o programa.
