import random
aleatorio = []
for cont in range(50):
    aleatorio.append(random.randint(0,100))

al = [random.randint(0,100)for cont in range(50)]
quadrados = [num**2 for num in range(1,11)]
lista = ['José','Jair','Maira','Mauro','João']
nome_J = [nome for nome in lista if nome[0] == 'J']
nomes = [nome for nome in lista if nome[0] == 'J']