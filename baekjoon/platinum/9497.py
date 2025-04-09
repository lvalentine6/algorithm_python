import math
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

if n == 1 or m == 1:
    print(max(n, m))
    exit()

g = math.gcd(n - 1, m - 1)
a = (n - 1) // g
b = (m - 1) // g
result = ((a + 1) * (b + 1)) // 2 + a * b * (g - 1)

print(result)
