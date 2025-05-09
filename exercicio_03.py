# exercicio_03.py

print("--- Calculadora de IMC (Índice de Massa Corporal) ---")

# Coleta o nome
nome = input("Por favor, digite seu nome: ")

# Coleta a altura
while True:
    try:
        altura_str = input(f"Olá {nome}, digite sua altura em metros (ex: 1.75): ")
        altura = float(altura_str)
        if altura <= 0:
            print("A altura deve ser um valor positivo. Por favor, tente novamente.")
        else:
            break  # Sai do loop se a altura for válida
    except ValueError:
        print(f"Entrada inválida ('{altura_str}'). Por favor, digite um número para a altura.")

# Coleta o peso
while True:
    try:
        peso_str = input(f"Agora, {nome}, digite seu peso em quilogramas (ex: 68.5): ")
        peso = float(peso_str)
        if peso <= 0:
            print("O peso deve ser um valor positivo. Por favor, tente novamente.")
        else:
            break # Sai do loop se o peso for válido
    except ValueError:
        print(f"Entrada inválida ('{peso_str}'). Por favor, digite um número para o peso.")

# O calculo usado para IMC é o seguinte:
# IMC = peso / (altura * altura)
# É importante garantir que altura não seja zero
imc = peso / (altura ** 2)  # altura ** 2 é o mesmo que altura * altura

# Exibe as informações coletadas e o resultado do calculo IMC
print("\n--- Resultados ---")
print(f"Nome: {nome}")
print(f"Altura: {altura:.2f} m")
print(f"Peso: {peso:.1f} kg")
print(f"Seu IMC é: {imc:.2f}") # Formata o IMC para exibir até 2 casas decimais

# Classificação do IMC após o calculo:
if imc < 18.5:
    print("Interpretação: Abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Interpretação: Peso normal.")
elif 25 <= imc < 29.9:
    print("Interpretação: Sobrepeso.")
elif 30 <= imc < 34.9:
    print("Interpretação: Obesidade Grau I.")
elif 35 <= imc < 39.9:
    print("Interpretação: Obesidade Grau II.")
else: # IMC >= 40
    print("Interpretação: Obesidade Grau III (Mórbida).")

print("\nLembre-se: O IMC é apenas um indicador. Consulte um profissional de saúde para uma avaliação completa.")