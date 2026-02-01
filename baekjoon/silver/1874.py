import sys

input = sys.stdin.readline

n = int(input().strip())
targets = []

for _ in range(n):
    targets.append(int(input().strip()))

_stack = []
result = []
num = 1
target_idx = 0
answer = []

while True:
    if len(targets) <= target_idx:
        break
    elif num < targets[target_idx]:
        _stack.append(num)
        num += 1
        answer.append('+')
    elif num == targets[target_idx]:
        result.append(num)
        target_idx += 1
        num += 1
        answer.append('+')
        answer.append('-')
    elif _stack and _stack[-1] == targets[target_idx]:
        result.append(_stack.pop())
        target_idx += 1
        answer.append('-')
    elif _stack and _stack[-1] != targets[target_idx]:
        answer = ['NO']
        break

for i in answer:
    print(i)