from random import randint
def EntradaDeCarros (placas,vagas):
    placa = input("Digite a placa e seu veiculo: ").upper()
    if placa in placas:
        print("Veiculo já cadastrado")
    else:
        veiculo_castrado = False
        while not veiculo_castrado:
            vaga = randint(0,100)
            if vaga not in vagas:
                vagas[vaga] = placa
                placas[placa] = vaga
                print(f"Veiculo cadastrado a vaga {vaga}")
                veiculo_castrado = True
    return placas,vagas

#programa principal
placas = {} 
vagas = {}
placas,vagas = EntradaDeCarros(placas,vagas)
placas,vagas = EntradaDeCarros(placas,vagas)
placas,vagas = EntradaDeCarros(placas,vagas)
placas,vagas = EntradaDeCarros(placas,vagas)
placas,vagas = EntradaDeCarros(placas,vagas)