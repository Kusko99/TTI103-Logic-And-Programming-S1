#s = 'Vitor2'
#s[0].isupper -> True
#s[1].islower -> True
#s[-1].isdigit -> True
#digita sua senha até ela ser válida
#para ser válida minimo 7 caracteres, conter uma letra maicula, uma letra minuscula e um digito

senha_ok = False
senha_upper = False
senha_lower = False
senha_digit = False
while not senha_ok:
    while True:
        senha = input("Digite sua senha: ")
        if len(senha) < 7:
            print("Sua senha deve ter 7 caracteres")
            break
        for letra in senha:
            x = letra.isupper()
            if x == True:
                senha_upper = True
        for letra in senha:
            x = letra.islower()
            if x == True:
                senha_lower = True
        for letra in senha:
            x = letra.isdigit()
            if x == True:
                senha_digit = True
        if (senha_digit == True and senha_upper == True and senha_lower == True):
            print("SENHA VALÍDA = )")
            print(senha)
            entrada_ok = True
        elif senha_upper == False:
            print("Sua senha deve conter ao menos uma letra maiscula")
        elif senha_lower == False:
            print("Sua senha deve conter ao menos uma letra minuscula")
        elif senha_digit == False:
            print("Sua senha deve conter ao menos um número")
