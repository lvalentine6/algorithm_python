def move(t, prev, nxt, mcnt, pointer):
    cnt = 0
    while cnt < mcnt:
        if t == 0:
            pointer = nxt[pointer]
        else:
            pointer = prev[pointer]
        cnt += 1

    return pointer


def solution(n, k, cmd):
    answer = ''

    prev = [i for i in range(n - 1)]
    prev.insert(0, -1)
    nxt = [i if i < n else -1 for i in range(1, n + 1)]
    stack = []
    pointer = k

    for c in cmd:
        command = c[0]
        if command == 'U':
            tmp = c.split(' ')
            pointer = move(1, prev, nxt, int(tmp[1]), pointer)
        elif command == 'D':
            tmp = c.split(' ')
            pointer = move(0, prev, nxt, int(tmp[1]), pointer)
        elif command == 'C':
            stack.append((pointer, prev[pointer], nxt[pointer]))

            if prev[pointer] != -1:
                nxt[prev[pointer]] = nxt[pointer]
            if nxt[pointer] != -1:
                prev[nxt[pointer]] = prev[pointer]

            if nxt[pointer] != -1:
                pointer = nxt[pointer]
            else:
                pointer = prev[pointer]
        elif command == 'Z':
            restore, pre, nx = stack.pop()
            if pre != -1:
                nxt[pre] = restore
            if nx != -1:
                prev[nx] = restore

    result = ['O' for _ in range(n)]

    for a, b, c in stack:
        result[a] = 'X'

    answer = ''.join(result)

    return answer


if __name__ == '__main__':
    solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
