def recur(idx, benefit):
    global answer

    if idx == n:
        answer = max(answer, benefit)
        return

    if idx > n:
        return

    recur(idx + lst[idx][0], benefit + lst[idx][1])

    recur(idx + 1, benefit)


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
answer = 0

recur(0, 0)

print(answer)
