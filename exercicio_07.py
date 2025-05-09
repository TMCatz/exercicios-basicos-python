# exercicio_07.py

print("--- Calculadora de Fatorial ---")

# Coleta um número inteiro
while True:
    try:
        entrada_str = input("Digite um número inteiro para calcular o seu fatorial: ")
        numero = int(entrada_str)
        break # Sai do loop se a conversão para inteiro for bem-sucedida
    except ValueError:
        print(f"Entrada inválida ('{entrada_str}'). Por favor, digite um número INTEIRO.")
    except Exception as e:
        # Captura outros erros inesperados durante o input, porém, menos comum.
        print(f"Ocorreu um erro inesperado durante a entrada: {e}")

print("----------------------------------------------------")

# Calcular e exibir o fatorial com base no número fornecido
if numero < 0:
    print(f"Não é possível calcular o fatorial de um número negativo ({numero}).")
elif numero == 0:
    # Por definição, o fatorial de 0 é 1.
    print(f"O fatorial de 0 (0!) é 1.")
else:  # O número é positivo (numero > 0)
    fatorial_resultado = 1
    # O fatorial de n (n!) é n * (n-1) * (n-2) * ... * 1.
    # Podemos calcular iterativamente:
    for i in range(1, numero + 1):
        fatorial_resultado *= i  # Equivalente a: fatorial_resultado = fatorial_resultado * i
    
    print(f"O fatorial de {numero} ({numero}!) é {fatorial_resultado}.")

print("----------------------------------------------------")