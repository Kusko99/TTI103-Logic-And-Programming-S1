testes = int(input())
for contas in range(testes):
    a,b,c = input().split()
    a=float(a)
    b=float(b)
    c=float(c)
    media=((a*2)+(b*3)+(c*5))/10
    print(f'{media:.1f}')