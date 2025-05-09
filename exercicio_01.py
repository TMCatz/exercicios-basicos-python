# exercicio_01.py

# Coleta o nome
nome = input("Por favor, digite seu nome: ")

# Coletar a altura
# Usando float() para permitir alturas com casas decimais (ex: 1.75)
altura_str = input("Digite sua altura em metros (ex: 1.75): ")
try:
    altura = float(altura_str)
except ValueError:
    print(f"Valor inválido para altura: '{altura_str}'. Usando 0.0 como padrão.")
    altura = 0.0


# Coleta o peso
# Usando float() para permitir pesos com casas decimais (ex: 68.5)
peso_str = input("Digite seu peso em quilogramas (ex: 68.5): ")
try:
    peso = float(peso_str)
except ValueError:
    print(f"Valor inválido para peso: '{peso_str}'. Usando 0.0 como padrão.")
    peso = 0.0

# Exibe as informações coletadas na tela
print("\n--- Informações Coletadas ---")
print(f"Nome: {nome}")
print(f"Altura: {altura:.2f} m") # Formata a altura para exibir 2 casas decimais
print(f"Peso: {peso:.1f} kg")    # Formata o peso para exibir 1 casa decimal
