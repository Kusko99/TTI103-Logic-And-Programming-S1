A,B,C=input().split()
A=float(A)
B=float(B)
C=float(C)
if (abs(B-C) < A and A < (B+C)) and (abs(A-C)<B and B < (A+C)) and(abs(A-B) <C and C< (A+B) ): 
    perimetro = A + B + C
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((A+B)*C)/2
    print(f'Area = {area:.1f}')