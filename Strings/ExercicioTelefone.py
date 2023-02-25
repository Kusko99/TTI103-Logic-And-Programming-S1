def filtro(telefone):
    pos = telefone.find('-')
    return telefone[pos+1:]

def traduzir(msg):
    msg = msg.upper()
    tel = ' '
    for letra in msg:
        if letra == 'A' or letra == 'B' or letra == 'C':
            tel  += 2
        elif letra == 'D' or letra == 'E' or letra == 'F':
            tel += 3
        elif letra == 'G' or letra == 'H' or letra == 'I':
            tel += 4
        elif letra == 'J' or letra == 'K' or letra == 'L':
            tel += 5
        elif letra == 'M' or letra == 'N' or letra == 'O':
            tel += 6
        elif letra == 'P' or letra == 'Q' or letra == 'R' or letra == 'S':
            tel += 7
        elif letra == 'T' or letra == 'U' or letra == 'V':
            tel += 8
        elif letra == 'W' or letra == 'X' or letra == 'Y' or letra == 'Z':
            tel += 9
        else:
            tel += '-'
        return '555' + tel


tel = '555-GET-FOOD'
print(traduzir(filtro(tel)))