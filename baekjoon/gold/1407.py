import math

a, b = map(int, input().split())
a -= 1

def cal(num):
    count = 0
    count += num
    for i in range(1, 99):
        count += int((num // math.pow(2, i)) * (math.pow(2, i) - math.pow(2, i - 1)))

    return count

print(cal(b) - cal(a))
