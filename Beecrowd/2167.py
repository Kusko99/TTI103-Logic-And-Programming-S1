medidas = int(input())
RPM = list(map(int,input().split()))
queda = 0
for teste in range(len(RPM)):
    if RPM[teste] < RPM[teste-1]:
        queda = teste + 1
        break
    else:
        RPM_Atual= RPM[teste]
print(queda)