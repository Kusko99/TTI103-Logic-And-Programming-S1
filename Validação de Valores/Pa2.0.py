#Função de validação de entrada
def EntradaReal(msg,erro):
    while not entradaOk:
        try:
            valor = float(input(msg))
            entradaOk = True
        except:
            print(erro)
#primeiro termo da PA
msg = "Primeiro termo da PA: "
erro = "ERRO, digite um número real!!"
a1 = EntradaReal(msg,erro)
#razão da PA
msg = "razão da PA: "
erro = "ERRO, digite um número real!!"
razao = EntradaReal(msg,erro)
n = 100
#Função de soma da PA
def SomaPA(primeiro,razao,elementos):
    ultimo = primeiro+(elementos-1)*razao
    return elementos*(primeiro+ultimo)/2
#Soma dos 100 primeiros termos da PA
n = 100
print(f"A soma dos {n} primeiros termos da PA vale {SomaPA(a1,razao,n)}")