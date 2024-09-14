def solution(board, h, w):
    answer = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]

        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board):
            continue

        if board[nx][ny] == board[h][w]:
            answer += 1

    return answer
