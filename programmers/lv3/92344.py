def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])

    # 차분배열 초기화
    diff = [[0 for _ in range(m + 2)] for _ in range(n + 2)]

    # 차분 배열 업데이트
    for t, r1, c1, r2, c2, num in skill:
        if t == 1:
            num = -num

        diff[r1][c1] += num
        diff[r1][c2 + 1] -= num
        diff[r2 + 1][c1] -= num
        diff[r2 + 1][c2 + 1] += num

    # 차분배열 가로 방향으로 누적합 적용
    for i in range(n + 1):
        for j in range(1, m + 1):
            diff[i][j] += diff[i][j - 1]

    # 차분배열 세로 방향으로 누적합 적용
    for j in range(m + 1):
        for i in range(1, n + 1):
            diff[i][j] += diff[i - 1][j]

    # 원본 배열에 적용하면서 정답체크
    for i in range(n):
        for j in range(m):
            board[i][j] += diff[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
