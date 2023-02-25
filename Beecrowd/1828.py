partidas = int(input())
gritos_do_sheldon = []
for patidas in range(partidas):
    sheldon, raj = input().split()
    if sheldon == "tesoura":
        if raj == "papel":
            gritos_do_sheldon.append("Bazinga!")
        elif raj == "Spock":
            gritos_do_sheldon.append("Raj trapaceou!")
        elif raj == "lagarto":
            gritos_do_sheldon.append("Bazinga!")
        elif raj == "pedra":
            gritos_do_sheldon.append("Raj trapaceou!")
        elif raj == "tesoura":
            gritos_do_sheldon.append("De novo!")
    if sheldon == "papel":
        if raj == "papel":
            gritos_do_sheldon.append("De novo!")
        elif raj == "Spock":
            gritos_do_sheldon.append("Bazinga!")
        elif raj == "lagarto":
            gritos_do_sheldon.append("Raj trapaceou!")
        elif raj == "pedra":
            gritos_do_sheldon.append("Bazinga!")
        elif raj == "tesoura":
            gritos_do_sheldon.append("Raj trapaceou!")
    
