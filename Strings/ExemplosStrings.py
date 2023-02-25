txt = 'Mauá CIC-sIN'
for letra in txt:
    print(letra)

'hello'
"hello"
'''hello'''
'''My friend to to me: "I want Domino's Pizza"'''

def imprimiMensagem(txt):
    '''Função para imprimir uma
    mensagem'''
    print(txt)

msg = 'cHupa Fei'
print(msg)
print(msg.upper())
print(msg.lower())

msg = 'chupa fei'
print(msg)
txt = msg.upper()
print(txt)
print(txt==msg)

ms = 'PUTA AULA CHATA...'
print(ms)
txt = ms.lower()
print(txt)

msg = 'PUTA AULA CHATA...'
txt = msg.split()
print(msg)
txt = msg.split('.')
print(txt)
txt = msg.split('A')
print(txt)
txt = msg.split(' ')
print(txt)

nome = 'José Antõnio da Silva'
print(nome.upper())
print(nome.capitalize())
print(nome.capitalize().split())
print(nome.count('o'))
print(nome.count('O'))
print('s' in nome)

'F+F-FFf+F-'

txt = 'Vou escrever qualquer coisa'
print(txt.find('u'))
print(txt.find('ue'))

txt = 'vitor.alves@maua.br'
pos = txt.find('@')
user = txt[0:pos]
domain = txt[pos+1:]
print(user)
print(domain)

txt = 'vitor.alves@maua.br'
print(txt.center(40))
print(txt.center(40,'*'))
print(txt.isalnum())
txt = 'vitor.alves maua.br'
print(txt.isalnum())
txt = 'vitor.alvesmaua.br'
print(txt.isalnum())
txt = 'vitoralvesmauabr'
print(txt.isalnum())
txt = 'vitorale23x_vesmauabr'
print(txt.isalnum())
txt = 'vitoralvesmauábr'
print(txt.isalnum())
print("\n")
txt = '23'
print(txt.isnumeric())
print(txt.isdecimal())
print(txt.isdigit())
print(txt.isalpha())
print("\n")
txt = 'ra'
print(txt.isnumeric())
print(txt.isdecimal())
print(txt.isdigit())
print(txt.isalpha())
print("\n")
txt = '2'
print(txt.isnumeric())
print(txt.isdecimal())
print(txt.isdigit())
print(txt.isalpha())
print("\n")
txt = '23.96'
print(txt.isnumeric())
print(txt.isdecimal())
print(txt.isdigit())
print(txt.isalpha())

