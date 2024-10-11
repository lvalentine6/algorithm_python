def recur(idx, w, v):
    global answer

    if w > k:
        return

    if idx == n:
        answer = max(answer, v)
        return

    recur(idx + 1, w + lst[idx][0], v + lst[idx][1])

    recur(idx + 1, w, v)

n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
answer = 0

recur(0, 0, 0)

print(answer)