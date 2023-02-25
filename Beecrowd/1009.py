nome = input()
salario_fixo = float(input())
total_de_vendas = float(input())
comissao = total_de_vendas*0.15
salario = salario_fixo+comissao
print(f"TOTAL = R$ {salario:.2f}")