#entrada
segundo = int(input('Digite o tempo em segundos: '))
#processamento
hora = segundo//3600
minuto = segundo % 3600 // 60
segundo = segundo % 3600 % 60
#saída
'''tempo = (hora,minuto,segundo)
print('O seu tempo será: ' tempo)'''
print (f'''O intervalo tem:
       {hora} horas
       {minuto} minutos
       {segundo} segundo''')