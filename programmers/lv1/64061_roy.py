def solution(board, moves):
    answer = 0

    stack = []

    for col in moves:
        for row in board:
            if row[col - 1] != 0:
                if stack and stack[-1] == row[col - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(row[col - 1])
                row[col - 1] = 0
                break
    return answer
