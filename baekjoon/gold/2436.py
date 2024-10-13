import math

a, b = map(int, input().split())

mul = b // a
sqrt_mul = int(math.sqrt(mul))

for i in range(sqrt_mul, 0, -1):
    if mul % i == 0:
        j = mul // i
        if math.gcd(i, j) == 1:
            print(i * a, j * a)
            break
