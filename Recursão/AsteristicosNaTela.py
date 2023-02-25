def ShowAstericos (n):
    if n > 1:
        ShowAstericos(n-1)
    return print('*'*n)

n = int(input("Digite n: "))
ShowAstericos(n)