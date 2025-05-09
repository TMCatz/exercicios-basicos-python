# Python: 10 Desafios de Programação 🐍

Bem-vindo(a) ao meu repositório de exercícios de Python! Este espaço registra minha jornada de aprendizado e prática com a linguagem Python, resolvendo 10 problemas que cobrem conceitos fundamentais da programação.

A descrição original deste repositório é: "Exercícios de Python cobrindo entrada/saída de dados, condicionais, loops e funções básicas." E é exatamente isso que você encontrará aqui, com cada desafio construído passo a passo.

## 🛠️ Sobre este Repositório

* **Tecnologia Principal:** Python 3
* **Estrutura:** Cada exercício está contido em um arquivo `exercicio_XX.py` individual. Alguns exercícios, como o 07, também possuem uma versão `_completo.py` que explora funcionalidades adicionais ou uma estrutura de código mais robusta.
* **Como Executar:** Para rodar qualquer um dos scripts, navegue até o diretório do arquivo no seu terminal e execute:
    ```bash
    python nome_do_arquivo.py
    ```
    (Ex: `python exercicio_01.py`)

## 🚀 Os Desafios (Exercícios Detalhados)

Abaixo você encontra a descrição de cada um dos 10 exercícios e os principais conceitos de Python que foram praticados em cada um deles:

---

1.  **`exercicio_01.py`**: Coleta nome, altura e peso do usuário e os exibe na tela.
    * **Principais Conceitos Praticados:**
        * Entrada de dados com `input()`.
        * Armazenamento de dados em variáveis.
        * Conversão de tipos de dados (`float()`).
        * Tratamento básico de erros com `try-except ValueError`.
        * Saída de dados formatada com `print()` e f-strings.

---

2.  **`exercicio_02.py`**: Coleta dois números e verifica qual o maior deles.
    * **Principais Conceitos Praticados:**
        * Entrada de dados e conversão para `float()`.
        * Estruturas condicionais `if-elif-else`.
        * Operadores de comparação (`>`, `==`).
        * Loop `while True` com `break` para garantir entrada válida.
        * Tratamento de `ValueError`.

---

3.  **`exercicio_03.py`**: Coleta nome, altura e peso do usuário, calcula o IMC e classifica o resultado.
    * **Principais Conceitos Praticados:**
        * Cálculo matemático com base em fórmula (IMC).
        * Validação de entrada (valores positivos para altura e peso).
        * Múltiplas condições com `if-elif-else` para classificação.
        * Interação contínua e feedback ao usuário durante a coleta de dados.

---

4.  **`exercicio_04.py`**: Simula a compra em uma quitanda, calculando o valor total de bananas com preço condicional por quantidade.
    * **Principais Conceitos Praticados:**
        * Lógica de negócios com preços condicionais (`if-else`).
        * Conversão para `int()` para quantidades.
        * Cálculo de valor total.
        * Formatação de saída para valores monetários (R$).
        * Mensagens interativas e personalizadas (ex: para 0 bananas).

---

5.  **`exercicio_05.py`**: Coleta os valores de três ângulos de um triângulo e o classifica como Acutângulo, Retângulo ou Obtusângulo.
    * **Principais Conceitos Praticados:**
        * Criação e uso de **funções** (`def`) para modularizar a coleta de dados.
        * Validação da soma dos ângulos (deve ser 180°).
        * Validação de ângulos positivos.
        * Lógica condicional complexa com `if-elif-else` e operadores `or`.
        * Comparação com números de ponto flutuante (`float`).

---

6.  **`exercicio_06.py`**: Calcula a média aritmética de valores inteiros positivos, encerrando a leitura com um valor negativo.
    * **Principais Conceitos Praticados:**
        * Loop `while True` para leitura contínua de dados.
        * Condição de parada do loop com `break`.
        * Acumulação de soma e contagem de valores.
        * Tratamento do caso de nenhuma entrada positiva (evitar divisão por zero).
        * Ignorar valores não positivos (zero) para o cálculo da média de positivos.

---

7.  **`exercicio_07.py`** e **`exercicio_07_completo.py`**: Lê um número e exibe seu fatorial (considerando 0! = 1 e fatorial de negativos não existente).
    * **`exercicio_07.py` (Versão base):**
        * Tratamento dos casos específicos (negativo, zero, positivo) com `if-elif-else`.
        * Cálculo iterativo do fatorial usando loop `for`.
    * **`exercicio_07_completo.py` (Versão Aprimorada):**
        * Todos os conceitos da versão base.
        * Modularização da lógica de cálculo em uma **função** (`calcular_fatorial`).
        * Loop `while True` para permitir **múltiplos cálculos** em uma sessão.
        * Implementação da opção para o usuário **sair** do programa (`input('sair')` e `exit()`).

---

8.  **`exercicio_08.py`**: Coleta três notas de um aluno, calcula a média e exibe a situação (Aprovado, Exame Final, Reprovado), com melhorias interativas.
    * **Principais Conceitos Praticados:**
        * Modularização com **funções** para coleta de notas.
        * Validação de intervalo para notas (0 a 10).
        * **Personalização da interação** com o nome do aluno.
        * Cálculo de média.
        * Mensagens de feedback e situação mais **empáticas e detalhadas**.
        * Loop `while True` para processar **múltiplos alunos**.
        * Opção para o usuário **continuar ou sair**.

---

9.  **`exercicio_09.py`**: Verifica se uma determinada letra (única) é vogal ou consoante.
    * **Principais Conceitos Praticados:**
        * Validação do tamanho da entrada (`len()`).
        * Conversão para minúsculas (`str.lower()`) para tratamento case-insensitive.
        * Verificação se é uma letra do alfabeto (ex: `'a' <= letra <= 'z'`).
        * Uso do operador `in` para verificar pertencimento a um conjunto de vogais.
        * Mensagens de erro claras para entradas inválidas.

---

10. **`exercicio_10.py`**: Verifica se o resultado da divisão entre dois números inteiros é par ou ímpar.
    * **Principais Conceitos Praticados:**
        * Coleta de dois números inteiros.
        * Tratamento crucial da **divisão por zero**.
        * Uso do operador módulo (`%`) para verificar se a divisão é exata.
        * Se exata, cálculo do quociente inteiro (`//`).
        * Uso do operador módulo (`% 2`) para determinar a paridade do quociente inteiro.
        * Lógica para informar que a paridade não se aplica se o resultado da divisão não for inteiro.

---

## 🌟 Considerações Finais

Este projeto foi uma excelente oportunidade para solidificar meu conhecimento em Python. Cada exercício apresentou um pequeno quebra-cabeça que me permitiu explorar diferentes facetas da linguagem.

Sinta-se à vontade para explorar os códigos!

---

Nathan
9 de Maio de 2025
