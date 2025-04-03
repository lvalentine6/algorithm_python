def solution(s):
    answer = []

    for i in s:
        stack = []
        lst = list(i)
        cnt = 0

        for l in lst:
            stack.append(l)

            if len(stack) >= 3:
                f = stack[-3]
                s = stack[-2]
                t = stack[-1]

                if f + s + t == '110':
                    for _ in range(3):
                        stack.pop()
                    cnt += 1

        last_zero = -1
        for j in range(len(stack) - 1, -1, -1):
            if stack[j] == '0':
                last_zero = j
                break

        if last_zero == -1:
            answer.append('110' * cnt + ''.join(stack))
        else:
            answer.append(''.join(stack[:last_zero + 1]) + '110' * cnt + ''.join(stack[last_zero + 1:]))

    return answer