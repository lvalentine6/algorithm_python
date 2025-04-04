import itertools


def check(weak, visited):
    return all(visited[w] for w in weak)


def calculate(n, start, dist, direction, visited):
    visited = visited[:]
    visited[start] = True

    if direction == 0:
        while dist > 0:
            start += 1
            dist -= 1
            if start >= n:
                start %= n
            visited[start] = True
    else:
        while dist > 0:
            start -= 1
            dist -= 1
            if start < 0:
                start = n + start
            visited[start] = True

    return visited


def search(n, weak, friends, permutations, visited, f_idx):
    if check(weak, visited):
        return True

    if f_idx >= len(friends):
        return False

    for d in range(2):
        new_visited = calculate(n, permutations[f_idx], friends[f_idx], d, visited)
        if search(n, weak, friends, permutations, new_visited, f_idx + 1):
            return True


def solution(n, weak, dist):
    answer = 1
    dist.sort(reverse=True)

    for i in range(1, len(dist) + 1):
        friends = dist[:i]
        permutations = itertools.permutations(weak, i)

        for p in permutations:
            visited = [False for _ in range(n + 1)]
            if search(n, weak, friends, p, visited, 0):
                return answer

        answer += 1

    return -1