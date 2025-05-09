# exercicio_08.py

def coletar_nota(numero_da_nota):
    """Coleta e valida uma nota do tipo (float)."""
    while True:
        try:
            nota_str = input(f"Digite a {numero_da_nota}ª nota: ")
            nota_aluno = float(nota_str)
            if not (0 <= nota_aluno <= 10):
                 print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
                 continue # Pede a nota novamente
            return nota_aluno
        except ValueError:
            print(f"Entrada inválida ('{nota_str}'). Por favor, digite um valor numérico para a nota.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            continue # Mesmo após ter ocorrido um erro o programa continua

print("--- Calculadora de Média e Situação do Aluno ---")
print("Por favor, insira três notas para que seja calculada a média do aluno.")

# Coleta as três notas
n1 = coletar_nota(1)
n2 = coletar_nota(2)
n3 = coletar_nota(3)

# Calcula a média aritmética
media_final = (n1 + n2 + n3) / 3

# Determina a situação do aluno com base na média
situacao = ""
if media_final >= 7.0:
    situacao = "Aprovado"
elif media_final >= 4.0:  # Esta condição é verificada se media_final < 7.0
    situacao = "Exame Final"
else:  # Neste caso, media_final < 4.0
    situacao = "Reprovado"

# Exibir as notas, a média e a situação final
print("\n---------- Resultado Final ----------")
print(f"Notas fornecidas: {n1:.1f}, {n2:.1f}, {n3:.1f}")
print(f"Média final do aluno: {media_final:.1f}") # Exibindo com uma casa decimal
print(f"Situação do aluno: {situacao}")
print("-----------------------------------")