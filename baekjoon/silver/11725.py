import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for i in range(n - 1):
    left, right = map(int, input().split())
    tree[left].append(right)
    tree[right].append(left)

queue = deque([1])
parent[1] = -1

while queue:
    current = queue.popleft()
    for nxt in tree[current]:
        if parent[nxt] == 0:
            parent[nxt] = current
            queue.append(nxt)

for i in range(2, len(parent)):
    print(parent[i])
