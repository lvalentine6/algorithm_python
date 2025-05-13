import sys

input = sys.stdin.readline
n = int(input())
answer = 0

is_prime = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

primes = [i for i, val in enumerate(is_prime) if val]

left = right = _sum = 0
while True:
    if _sum >= n:
        if _sum == n:
            answer += 1
        _sum -= primes[left]
        left += 1
    elif right == len(primes):
        break
    else:
        _sum += primes[right]
        right += 1

print(answer)
