import math
N = int(input())
P = N/math.log(N,math.e)
M = 1.25506*(N/math.log(N,math.e))
print(f"{P:.1f} {M:.1f}")