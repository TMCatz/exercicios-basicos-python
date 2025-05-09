# exercicio_07+completo.py

def calcular_fatorial(numero_para_calcular):
    """
    Calcula o fatorial de um número inteiro não negativo.
    Retorna o valor do fatorial ou None se o fatorial não for definido (para negativos).
    """
    if numero_para_calcular < 0:
        return None  # Indica que o fatorial não é definido para negativos
    elif numero_para_calcular == 0:
        return 1
    else:
        resultado_fatorial = 1
        for i in range(1, numero_para_calcular + 1):
            resultado_fatorial *= i
        return resultado_fatorial

print("--- Calculadora de Fatorial Interativa ---")

while True: # Loop para permitir múltiplos cálculos sem ter a necessidade de reiniciar o programa
    # Coleta um número inteiro do usuário
    while True: # Loop para garantir que o input é válido
        try:
            entrada_str = input("\nDigite um número inteiro para calcular o seu fatorial (ou 'sair' para terminar): ")
            if entrada_str.lower() == 'sair':
                print("Encerrando a calculadora de fatorial. Até mais!")
                exit() # Encerra o programa
            
            numero = int(entrada_str)
            break # Sai do loop de entrada se a conversão para inteiro for bem-sucedida
        except ValueError:
            print(f"Entrada inválida ('{entrada_str}'). Por favor, digite um NÚMERO INTEIRO ou 'sair'.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado durante a entrada: {e}")


    print("----------------------------------------------------")
    
    resultado = calcular_fatorial(numero)

    if resultado is None: # Verificamos se a função retornou None (para negativos)
        print(f"Não é possível calcular o fatorial de um número negativo ({numero}).")
    else:
        # Para numero == 0 ou numero > 0, 'resultado' terá o valor do fatorial.
        print(f"O fatorial de {numero} ({numero}!) é {resultado}.")

    print("----------------------------------------------------")
    
    # A pergunta se quer continuar já está implícita pelo loop principal
    # e a opção de digitar 'sair'. Caso não digite 'sair', ele volta para o loop e pede outro número.
