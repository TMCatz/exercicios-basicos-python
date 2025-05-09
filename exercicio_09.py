# exercicio_09.py

# Teste com:
# Vogais minúsculas (a, e, i, o, u).
# Vogais maiúsculas (A, E, I, O, U).
# Consoantes minúsculas (b, c, d, x, z).
# Consoantes maiúsculas (B, C, D, X, Z).
# Números (ex: 1, 5).
# Símbolos (ex: $, #, !).
# Múltiplos caracteres (ex: "ab", "letra").
# Nenhuma entrada (apenas pressione Enter).

print("--- Verificador de Vogal ou Consoante ---")

# Coleta a letra
entrada_usuario = input("Digite uma única letra para verificar: ")

# Valida a entrada e classifica a letra
if len(entrada_usuario) == 1:
    letra = entrada_usuario.lower()  # Converte para minúscula para verificação case-insensitive

    # Verifica se o caractere é uma letra do alfabeto
    if 'a' <= letra <= 'z': # Simplificação
        # Definir as vogais (sem acentos)
        vogais = "aeiou"

        if letra in vogais:
            print(f"A letra '{entrada_usuario}' é uma VOGAL.")
        else:
            print(f"A letra '{entrada_usuario}' é uma CONSOANTE.")
    else:
        # Se não está no intervalo 'a'-'z' (após lower()), não é uma letra simples do alfabeto
        print(f"Entrada inválida: '{entrada_usuario}'. Isso não parece ser uma letra simples do alfabeto.")
        print("Por favor, digite apenas uma letra (sem números, símbolos ou acentos para que o programa funcione).")

elif len(entrada_usuario) == 0:
    print("Nenhuma entrada fornecida. Por favor, digite uma letra.")
else: # Mais de um caractere foi digitado
    print(f"Entrada inválida: '{entrada_usuario}'. Por favor, digite APENAS UMA letra.")

print("-----------------------------------------")