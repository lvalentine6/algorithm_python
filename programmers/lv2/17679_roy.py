def solution(m, n, board):
    answer = 0

    board = [list(i) for i in board]

    flag = False

    while not flag:
        visited = [[False for _ in range(n)] for _ in range(m)]

        for row in range(m - 1):
            for col in range(n - 1):
                if (board[row][col] == board[row][col + 1] == board[row + 1][col] == board[row + 1][col + 1]) and \
                        board[row][col] != '':
                    visited[row][col] = visited[row][col + 1] = visited[row + 1][col] = visited[row + 1][col + 1] = True

        cnt = 0
        for v in visited:
            cnt += v.count(True)
        answer += cnt

        new_board = [[board[row][col] if visited[row][col] == False else '' for col in range(n)] for row in range(m)]

        new_board = new_board[::-1]

        for row in range(m):
            for col in range(n):
                if new_board[row][col] == '':
                    for up in range(row, m):
                        if new_board[up][col]:
                            new_board[row][col] = new_board[up][col]
                            new_board[up][col] = ''
                            break
        new_board = new_board[::-1]

        if board == new_board:
            flag = True
        else:
            board = new_board

    return answer
