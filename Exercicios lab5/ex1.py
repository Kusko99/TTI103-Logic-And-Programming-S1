#entrada
PRIMEIRO_NUMERO = float(input("Digite o primeiro número: "))
SEGUNDO_NUMERO = float(input("Digite o segundo número: "))
TERCEIRO_NUMERO = float(input("Digite o terceiro número:"))
#processamento
RESULTADO = (PRIMEIRO_NUMERO + SEGUNDO_NUMERO)*TERCEIRO_NUMERO
#Saída
print(f'''A soma de {PRIMEIRO_NUMERO:.3f} com {SEGUNDO_NUMERO:.3f}
      multiplicada por {TERCEIRO_NUMERO:.3f} vale {RESULTADO:.3f}''')