string = input("Digite sua String: ")
string = string.lower()

vogais = 0
espacos = 0
consoantes = 0

vogais = ['a,e,i,o,u,á,à,ã,é,è,ê,ô,õ,ó,ò,ì,í,î']
consoantes = ['b,c,ç,d,f,g,h,j,k,l,m,n,o,p,q,r,s,t,v,w,x,y,z']

for letra in range(len(string)):
    if string[letra] in vogais:
        vogais += 1
    elif string[letra] in ' ':
        espacos += 1
    elif string[letra] in consoantes:
        consoantes += 1

print(vogais, espacos, consoantes)