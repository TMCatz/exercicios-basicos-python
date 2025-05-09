# exercicio_06.py

print("--- Calculadora de Média de Inteiros Positivos ---")
print("Digite números inteiros positivos um por um.")
print("Para finalizar a entrada de dados e calcular a média, basta digitar um número negativo.")
print("----------------------------------------------------")

soma_valores = 0
contador_valores_positivos = 0

while True:
    try:
        entrada_usuario = input(f"Digite o {contador_valores_positivos + 1}º valor (ou um número negativo para parar): ")
        valor_atual = int(entrada_usuario)

        if valor_atual < 0:
            print("Número negativo detectado. Encerrando a coleta de valores.")
            break  # Termina o loop

        if valor_atual > 0:
            soma_valores += valor_atual
            contador_valores_positivos += 1
            print(f"-> Valor {valor_atual} adicionado. Soma atual: {soma_valores}. Quantidade de positivos: {contador_valores_positivos}.")
        elif valor_atual == 0:
            # Zero não é positivo, então não entra na média de positivos.
            print("-> O número 0 não é positivo e não será considerado na média. Continue ou digite um negativo para sair.")
        # Não há 'else' aqui, pois o caso valor_atual < 0 já vai acontecer um 'break'.

    except ValueError:
        print(f"Atenção: Entrada inválida ('{entrada_usuario}'). Por favor, digite um número inteiro.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}") # Caso aconteça algum outro erro inesperado

# Após o loop, calcula e exibe a média dos números
print("----------------------------------------------------")
if contador_valores_positivos > 0:
    media_calculada = soma_valores / contador_valores_positivos
    print(f"Total de valores positivos inseridos: {contador_valores_positivos}")
    print(f"Soma dos valores positivos: {soma_valores}")
    print(f"Média aritmética dos valores positivos: {media_calculada:.2f}") # Calcula a média com 2 casas decimais
else:
    # Este bloco é executado se o primeiro número digitado for negativo,
    # ou se apenas zeros e depois um negativo forem digitados.
    print("Nenhum valor inteiro positivo foi inserido.")
    print("Não foi possível calcular a média.")

print("----------------------------------------------------")