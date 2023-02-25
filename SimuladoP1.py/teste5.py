valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
if valor1 == valor2 or valor1 > valor2:
    print(f"O maior valor é {valor1}")
elif valor1 < valor2:
    print(f"O maior valor é {valor2}")