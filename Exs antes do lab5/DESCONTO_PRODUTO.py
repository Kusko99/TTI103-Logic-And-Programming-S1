#variáveis
valor_produto = int(input("Digite o preço do produto: "))
desconto = int(input("Digite o desconto em porcentagem: "))
#processamento
desconto = desconto/100
valor_produto_final = valor_produto - (valor_produto * desconto)
#saída
print("O valor do produto com desconto será: ", valor_produto_final)