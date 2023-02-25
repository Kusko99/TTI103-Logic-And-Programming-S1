def entrada():
    notas = []
    entrada_ok = True
    while entrada_ok:
        try:
            while entrada_ok:
                a = float(input("Digite a sua nota: "))
                if a >= 0 and a <=100:
                    notas.append(a)
                else:
                    print("Só valem notas de 0 a 100")
                if len(notas) == 5:
                    entrada_ok = False
        except:
            print("Só valem notas de 0 a 100")
    return notas
def calculadora(notas):
    return sum(notas)/len(notas)   
notas = entrada()
media = calculadora(notas)
print(f"A média é : {media:.1f}")  