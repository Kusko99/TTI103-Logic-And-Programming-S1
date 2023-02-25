A,B=input().split()
#C,D=input().split()
#E,F=input().split()
A=float(A)
B=float(B)
#C=float(C)
#D=float(D)
#E=float(E)
#F=float(F)
Lista=[A,B]
Lista.sort()
Lista1=[]
while A != B:
    if A < B:
        Lista1.append(A)
        A += 1
    elif A <= 0 or B <= 0:
        pass
    elif B < A:
        Lista1.append(B)
        B+=1
Lista1.append(B)
print(Lista1)
    
