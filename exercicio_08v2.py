# exercicio_08v2.py (versão aprimorada)

def coletar_nota(numero_da_nota, nome_do_aluno=""):
    """Coleta e valida uma nota (float entre 0 e 10) do usuário."""
    aluno_prompt = f" para {nome_do_aluno}" if nome_do_aluno else "" # Adiciona nome
    while True:
        try:
            nota_str = input(f"Digite a {numero_da_nota}ª nota{aluno_prompt}: ")
            nota_aluno = float(nota_str)
            if not (0 <= nota_aluno <= 10):
                print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
                continue # Pede a nota novamente
            return nota_aluno
        except ValueError:
            print(f"Entrada inválida ('{nota_str}'). Por favor, digite um valor numérico para a nota.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            continue 

# --- Loop principal para processar múltiplos alunos ---
while True:
    print("\n--- Calculadora de Média e Situação do Aluno ---")
    
    nome_aluno = input("Digite o nome do(a) aluno(a) (ou deixe em branco para 'Aluno Anônimo'): ")
    if not nome_aluno.strip(): # Se o nome estiver vazio ou só com espaços
        nome_aluno = "Aluno(a) Anônimo(a)"

    print(f"\nPor favor, insira as três notas de {nome_aluno}.")

    # Coleta as três notas
    n1 = coletar_nota(1, nome_aluno)
    n2 = coletar_nota(2, nome_aluno)
    n3 = coletar_nota(3, nome_aluno)

    # Calcula a média aritmética
    media_final = (n1 + n2 + n3) / 3

    # Determina a situação do aluno com base na média e cria uma mensagem personalizada
    situacao_texto = ""
    mensagem_detalhada = ""

    if media_final >= 7.0:
        situacao_texto = "Aprovado(a)"
        mensagem_detalhada = f"Parabéns, {nome_aluno}! Você foi {situacao_texto.lower()} com média {media_final:.1f}."
    elif media_final >= 4.0:
        situacao_texto = "em Exame Final"
        mensagem_detalhada = f"{nome_aluno}, sua média foi {media_final:.1f}. Você está {situacao_texto}. Dedique-se aos estudos para a próxima etapa!"
    else:
        situacao_texto = "Reprovado(a)"
        mensagem_detalhada = f"{nome_aluno}, com média {media_final:.1f}, infelizmente você foi {situacao_texto.lower()}. Não desanime e prepare-se melhor para a próxima oportunidade."

    # Exibe as notas, a média e a situação final
    print("\n---------- Resultado Final ----------")
    print(f"Aluno(a): {nome_aluno}")
    print(f"Notas fornecidas: {n1:.1f}, {n2:.1f}, {n3:.1f}")
    print(f"Média final: {media_final:.1f}")
    print(f"Situação: {mensagem_detalhada}") # Exibe a mensagem mais completa
    print("-----------------------------------")

    # Perguntar se deseja continuar para outro aluno ou matéria
    resposta_continuar = input("\nDeseja calcular a média para outro(a) aluno(a)? (s/n): ")
    if resposta_continuar.lower() != 's':
        print("Encerrando o programa. Até mais!")
        break # Sai do loop principal