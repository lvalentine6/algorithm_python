import math

n = int(input())
lst = []

for i in range(2, int(math.sqrt(n)) + 1):
    while n % i == 0:
        lst.append(i)
        n //= i

if n > 2:
    lst.append(n)

print(len(lst))
print(*lst)
