def entrada():
    d = {}
    n = int(input("Quantos projetos serão digitados: "))
    for _ in range(n):
        cod = int(input("Digite o código do projetos: "))
        d[cod] = input("Quanto tempo o projeto levou: ")
    return d

def sorting(d):
    chaves = list(d.keys())
    chaves.sort()
    for i in range(len(chaves)):
        #print(d[chaves[i]])
        print(f"O projeto de id {chaves[i]} demorou {d[chaves[i]]}")

sorting(entrada())