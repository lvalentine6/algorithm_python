def search(n, position, cnt, visited, lst):
    if all(visited):
        result.append(cnt)
        return

    for i in range(n):
        if not visited[i] and lst[position][i] != 0:
            if cnt == 0 or cnt >= lst[position][i]:
                visited[i] = True
                search(n, i, cnt + lst[position][i], visited, lst)
                # visited[i] = False


def solution(n, costs):
    answer = 0

    lst = [[0 for _ in range(n)] for _ in range(n)]
    visited = [False for _ in range(n)]
    global result
    result = []

    for cost in costs:
        lst[cost[0]][cost[1]] = cost[2]
        lst[cost[1]][cost[0]] = cost[2]

    visited[0] = True
    search(n, 0, 0, visited, lst)

    print(result)

    return answer