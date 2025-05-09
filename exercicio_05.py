# exercicio_05.py

# Teste com diferentes combinações de ângulos:
# Acutângulo: 60, 60, 60 | 70, 50, 60
# Retângulo: 90, 45, 45 | 30, 60, 90
# Obtusângulo: 100, 40, 40 | 20, 120, 40
# Inválido (soma != 180): 50, 50, 50 | 90, 90, 10
# Inválido (ângulo <= 0): Teste digitar 0 ou um número negativo para um dos ângulos.
# Entradas não numéricas.

def angulos(numero_do_angulo):
    """Coleta um valor de ângulo (float positivo) do usuário."""
    while True:
        try:
            angulo_str = input(f"Digite o valor do ângulo {numero_do_angulo} (em graus): ")
            angulo = float(angulo_str)
            if angulo <= 0:
                print("O valor do ângulo deve ser positivo. Tente novamente.")
            else:
                return angulo
        except ValueError:
            print(f"Entrada inválida ('{angulo_str}'). Por favor, digite um número válido.")

print("--- Classificador de Triângulos (Com base nos Ângulos) ---")
print("Por favor, forneça os três ângulos do triângulo.")

# Coleta todos os três ângulos
a1 = angulos(1)
a2 = angulos(2)
a3 = angulos(3)

print(f"\nÂngulos fornecidos: {a1}°, {a2}°, {a3}°")

# Validar a soma dos ângulos
soma_dos_angulos = a1 + a2 + a3

if soma_dos_angulos == 180.0:
    print(f"Soma dos ângulos: {soma_dos_angulos}° (Válido para um triângulo).")

    # Classificação dos triângulos
    if a1 == 90.0 or a2 == 90.0 or a3 == 90.0:
        print("Classificação: Triângulo Retângulo (possui um ângulo reto igual a 90°).")
    elif a1 > 90.0 or a2 > 90.0 or a3 > 90.0:
        # Um triângulo só pode ter um ângulo obtuso.
        # Se tivesse mais de um, a soma excederia 180.
        # A verificação da soma = 180 já garante isso.
        print("Classificação: Triângulo Obtusângulo (possui um ângulo obtuso superior a 90°).")
    else:
        # Se não é retângulo nem obtusângulo, e a soma é 180°,
        # todos os ângulos devem ser menores que 90°.
        print("Classificação: Triângulo Acutângulo (todos os ângulos são agudos inferiores a 90°).")
else:
    print(f"Soma dos ângulos: {soma_dos_angulos}°.")
    print("Os ângulos fornecidos NÃO formam um triângulo válido, pois a soma dos ângulos internos deve ser 180°.")

print("--------------------------------------------------------")