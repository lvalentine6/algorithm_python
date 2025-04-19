class RoyStack():
    def __init__(self, capacity=1000):
        self.space = [None] * capacity
        self.index = 0

    def push(self, value):
        self.space.append(value)
        self.index += 1
        return

    def pop(self):
        if self.index == 0:
            return -1
        self.index -= 1
        return self.space[self.index]

    def size(self):
        return len(self.space)

    def empty(self):
        if not self.space:
            return 1
        return 0

    def top(self):
        if not self.space:
            return -1
        return self.space[-1]


import sys

FIRST_VALUE = 0
input = sys.stdin.readline
n = int(input())
roy_stack = RoyStack()

commands = {
    'push': lambda v: roy_stack.push(v[FIRST_VALUE]),
    'pop': lambda _: print(roy_stack.pop()),
    'size': lambda _: print(roy_stack.size()),
    'empty': lambda _: print(roy_stack.empty()),
    'top': lambda _: print(roy_stack.top())
}

for _ in range(n):
    command, *number = input().split()
    if command in commands:
        commands[command](number)
