n = int(input())
answer = 0

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if i + j + k == n:
                if k >= j + 2:
                    if i and j and k != 0:
                        if i % 2 == 0:
                            answer += 1

print(answer)
