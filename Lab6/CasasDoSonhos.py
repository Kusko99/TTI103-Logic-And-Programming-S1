#receber o salário, porcentagem a ser guradada e valor da casa
#devolver quanto tempo pra comprar a casa
#entrada
salario = float(input("Digite o valor do seu salário mensal: "))
guardar = float(input("Digite a porcentagem do salário a ser guardado: "))
valor_casa = float(input('Digite o valor da casa desejada: '))
#iniciação de variáveis
guardar = (guardar/100)
valor_guardado = salario*guardar
economizado = 0
entrada = 25/100
porc_casa = entrada*valor_casa
#poupanca = valor_guardado
juros_porcentagem = (0.5/100)
meses = 0
#while
while economizado < valor_casa:
    meses +=1
    economizado = valor_guardado = valor_guardado + (economizado*(1+juros_porcentagem))
print (f'Você deverá guardar por {meses} meses ')
