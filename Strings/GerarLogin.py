def entrada ():
    nome = input("Digite o seu nome: ")
    if len(nome) < 3:
        nome = verifica()
    sobrenome = input("Digite o seu sobrenome: ")
    ra = input("Digite o seu ra: ")
    return nome, sobrenome, ra

def stringArrumada (nome,sobrenome,ra):
    import string
    pont = string.punctuation
    nome = nome.translate(str.maketrans(' ',' ',pont))
    sobrenome = sobrenome.translate(str.maketrans(' ',' ',pont))
    ra = ra.translate(str.maketrans(' ',' ',pont))
    return nome, sobrenome,ra

def gerarSenha (nome,sobrenome,ra):
    senha = (nome[:3] + sobrenome[:3] + ra[-3:])

def verifica ():
    entrada_ok = False
    while not entrada_ok:
        print("Digite com 3 ou mais caracteres")
        verificar = input("Digite o novamente: ")
        if len(verificar) >= 3:
            entrada_ok = True
    return verificar

print(verifica())