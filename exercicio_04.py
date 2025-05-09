# exercicio_04.py

print("--- Quitanda do Zé - Promoção de Bananas ---")
print("Aproveite nossa promoção:")
print("- Comprando 3 ou mais bananas, cada uma sai por R$ 0,80.")
print("- Comprando menos de 3 bananas, cada uma sai por R$ 1,00.")
print("---------------------------------------------")

# Coleta a quantidade de bananas
while True:
    try:
        quantidade_str = input("Quantas bananas você gostaria de comprar? ")
        quantidade = int(quantidade_str)  # Bananas são contadas em unidades inteiras então não há necessidade de trocar para float
        
        if quantidade < 0:
            print("A quantidade não pode ser negativa. Por favor, digite um número válido.")
        else:
            break  
    except ValueError:
        print(f"Entrada inválida ('{quantidade_str}'). Por favor, digite um número inteiro.")

# Aqui é feita a definição do preço por banana e calcula o valor total
preco_unitario = 0.0
valor_total = 0.0
mensagem_preco_aplicado = ""
status_desconto = "" # Armazena a mensagem sobre o desconto

if quantidade > 0:  # Processa apenas se a quantidade for positiva
    if quantidade < 3:
        preco_unitario = 1.00
        mensagem_preco_aplicado = f"Para {quantidade} banana(s), o preço aplicado é R$ {preco_unitario:.2f} por unidade."
        status_desconto = "Compra sem desconto (menos de 3 unidades)."
    else:  # Quantidade >= 3
        preco_unitario = 0.80
        mensagem_preco_aplicado = f"Para {quantidade} bananas, o preço promocional aplicado é R$ {preco_unitario:.2f} por unidade."
        status_desconto = "Desconto promocional aplicado (3 ou mais unidades)!"
    
    valor_total = quantidade * preco_unitario
    print(mensagem_preco_aplicado) # Exibe a mensagem sobre o preço aqui
    
elif quantidade == 0:
    print("\nQue pena, não gostou de nenhum dos nossos cachos de banana? Esperamos sua próxima visita à Quitanda do Zé!")


# Exibir o resumo da compra
print("\n--- Resumo da Compra ---")
print(f"Quantidade de bananas: {quantidade}")

if quantidade > 0: # Mostrar preço unitário apenas se comprou algo e o preço foi definido
    print(f"Preço por banana (aplicado): R$ {preco_unitario:.2f}")
    print(f"Status do desconto: {status_desconto}")
    
print(f"Valor total da compra: R$ {valor_total:.2f}")
