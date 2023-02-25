def entrada(texto):
    x = int(input(texto))
    return x

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fator = num * fatorial(num-1)
        return fator

num = entrada("Digite o número para o fatorial: " )
print(f"O fatorial de {num} é : {fatorial(num)}")