#entrada
Tempo_Entrada = int(input('Digite o seu tempo em segundos: '))
#processamento
hora = Tempo_Entrada//3600
minutos = (Tempo_Entrada%3600)//60
segundos = Tempo_Entrada%60
#saída
print('O seu tempo será:',hora,minutos,segundos)
