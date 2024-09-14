def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    lst = []

    def dfs(row=0, col=0, cnt=1):
        if row == n - 1 and col == m - 1:
            lst.append(cnt)
            return

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(row + dr[i], col + dc[i], cnt + 1)
                visited[nr][nc] = False

    dfs()

    answer = min(lst) if lst else -1

    return answer
