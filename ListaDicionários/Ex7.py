paes = {"ATC003":5,"ATC006":5,"ATC009":5,"ATC030":5,"ATC001":10,"ATC004":10,"ATC007":10,
"ATC010":10,"ATC013":10,"ATC026":10,"ATC028":10,"ATC032":10,"ATC034":10,"ATC016":40,
"ATC018":40,"ATC020":40,"ATC022":40,"ATC024":40,"ATC036":40}

quanatas_pae = int(input("Quantas paes vc fez? "))
paes_inseridas = 0
horas = 0
while quanatas_pae > paes_inseridas:
        codigo = input("Digite o código da pae: ")
        if codigo in paes:
            cumprimu = input("Digite o conceito recibido (C/N): ")
            if cumprimu == "C":
                horas += paes[codigo]
                paes_inseridas += 1
        else:
            print("Comando ou código inseridos errados")
print(f"Cumpriu {horas} de 60 horas")