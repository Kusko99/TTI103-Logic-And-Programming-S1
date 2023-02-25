#s = 'Vitor2'
#s[0].isupper -> True
#s[1].islower -> True
#s[-1].isdigit -> True
#digita sua senha até ela ser válida
#para ser válida minimo 7 caracteres, conter uma letra maicula, uma letra minuscula e um digito
def main():
    senha_ok = False
    valida = 0
    while not senha_ok:
        while True:
            senha = input("Digite sua senha: ")
            if len(senha) < 7:
                print("Sua senha deve ter 7 caracteres")
                break
            else:
                valida += 1
            for letra in senha:
                x = letra.isupper()
                if x == True:
                    valida += 1
                    break
            for letra in senha:
                x = letra.islower()
                if x == True:
                    valida += 1
                    break
            for letra in senha:
                x = letra.isdigit()
                if x == True:
                    valida += 1
                    break
            if valida == 4:
                senha_ok = True
                break
            else:
                print("Sua senha deve ter uma letra maiscula, uma minuscula e um numero")
    print("SENHA VALÍDA = )")
    print(senha)
main()