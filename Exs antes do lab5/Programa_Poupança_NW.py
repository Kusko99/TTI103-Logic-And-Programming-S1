#entrada
R = float(input("DIgite o valor a taxa de juros em porcentagem: "))
N = int(input("A quantidade, em anos, a ser guardado: "))
F = float(input("A quantiade que gostaria de receber ao fim do periodo: "))
#processamento
P = F/((1+R)**N)
#saída
print('Para alcançar o seu objetivo você deve depositar um total de: ',P)


