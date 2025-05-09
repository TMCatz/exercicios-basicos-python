# exercicio_02.py

print("--- Qual Número é Maior? ---")

# Coleta o primeiro número
while True:
    try:
        num1_str = input("Digite o primeiro número: ")
        num1 = float(num1_str)  # Converte a entrada para float (permite decimais)
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print(f"Entrada inválida ('{num1_str}'). Por favor, digite um número válido.")

# Coleta o segundo número
while True:
    try:
        num2_str = input("Digite o segundo número: ")
        num2 = float(num2_str)  # Conversão do input para float
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print(f"Entrada inválida ('{num2_str}'). Por favor, digite um número válido.")

# Verifica qual número é o maior e mostra o resultado
print("\n--- Resultado ---")
if num1 > num2:
    print(f"O primeiro número ({num1}) é maior que o segundo número ({num2}).")
elif num2 > num1:
    print(f"O segundo número ({num2}) é maior que o primeiro número ({num1}).")
else:
    print(f"Os dois números são iguais ({num1}).")