#a,b,c = input().split()
#if a == 'vertebrado':
    #if b == 'ave':
        #if c == 'carnivoro':
            #print('aguia')
        #elif c == 'onivoro':
            #print('pomba')
    #elif b == 'mamifero':
        #if c == 'onivoro':
            #print('homem')
        #elif c == 'herbivoro':
            #print('vaca')
#elif a == 'invertebrado':
    #if b == 'inseto':
       # if c == 'hematofago':
          # print('pulga')
       # elif c == 'herbivoro':
           # print('lagarta')
   # elif b == 'anelidio':
       # if c == 'hematofago':
        #    print('sanguessuga')
        #elif c == 'onivoro':
           # print('minhoca')
a=input()
b=input()
c=input()
if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if c == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if b == 'inseto':
        if c == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if c == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')