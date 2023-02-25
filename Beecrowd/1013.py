a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
MaiorAB = (a+b+abs(a-b))/2
d = MaiorAB
MaiorDC = (d+c+abs(d-c))/2
print(f"{MaiorDC} eh o maior")