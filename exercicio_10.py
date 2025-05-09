# exercicio_10.py

# Teste com diversos pares de números:
# Resultado Inteiro Par: (Dividendo: 6, Divisor: 3 -> Res: 2 (Par) | Dividendo: 8, Divisor: 2 -> Res: 4 (Par))
# Resultado Inteiro Ímpar: (Dividendo: 9, Divisor: 3 -> Res: 3 (Ímpar) | Dividendo: 5, Divisor: 1 -> Res: 5 (Ímpar))
# Resultado Não Inteiro: (Dividendo: 5, Divisor: 2 -> Res: 2.5 | Dividendo: 7, Divisor: 3 -> Res: 2.33...)
# Divisão por Zero: (Dividendo: 10, Divisor: 0)
# Dividendo Zero: (Dividendo: 0, Divisor: 5 -> Res: 0 (Par))
# Entradas não numéricas.

def numero_inteiro(prompt_mensagem):
    """Coleta um número inteiro, com validação."""
    while True:
        try:
            entrada_str = input(prompt_mensagem)
            numero = int(entrada_str)
            return numero
        except ValueError:
            print(f"Entrada inválida ('{entrada_str}'). Por favor, digite um número INTEIRO.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado durante a entrada: {e}")

print("--- Verificador de Paridade do Resultado da Divisão ---")
print("Este programa verifica se o resultado da divisão entre dois inteiros é par ou ímpar.")
print("Nota: A paridade (par/ímpar) só se aplica se o resultado da divisão for um número inteiro.")
print("------------------------------------------------------------------------------------")

# Coleta os dois números inteiros
num1 = numero_inteiro("Digite o primeiro número inteiro (dividendo): ")
num2 = numero_inteiro("Digite o segundo número inteiro (divisor): ")

print(f"\nNúmeros fornecidos: Dividendo = {num1}, Divisor = {num2}")
print("------------------------------------------------------------------------------------")

# Verifica se o divisor é zero
if num2 == 0:
    print("Erro Crítico: Divisão por zero não é permitida!")
    print("Não é possível realizar a verificação.")
else:
    # Verifica se a divisão resulta em um número inteiro
    # Isso ocorre se o resto da divisão de num1 por num2 for 0
    if num1 % num2 == 0:
        # Se a divisão é exata, o quociente é um inteiro
        quociente_inteiro = num1 // num2  # Usando divisão inteira para garantir o tipo int

        print(f"A divisão de {num1} por {num2} é exata, resultando em: {quociente_inteiro}")

        # Agora, vai verificar se o quociente inteiro é par ou ímpar
        # Usando o resto da divisão por 2 (quociente_inteiro % 2)
        if quociente_inteiro % 2 == 0:
            print(f"O resultado da divisão ({quociente_inteiro}) é PAR.")
        else:
            print(f"O resultado da divisão ({quociente_inteiro}) é ÍMPAR.")
    else:
        # Caso o resultado da divisão não seja um número inteiro:
        resultado_decimal = num1 / num2
        print(f"A divisão de {num1} por {num2} resulta em {resultado_decimal:.2f} (um número não inteiro).")
        print("Como o resultado não é um número inteiro, a classificação de par ou ímpar não se aplica.")

print("------------------------------------------------------------------------------------")