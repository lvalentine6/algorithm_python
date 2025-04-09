import sys

input = sys.stdin.readline
lst = list(input().strip())
stack = []
target = ['(', '[', ')', ']']
last_char = []

for s in lst:
    if s == '(' or s == '[':
        stack.append(s)
        last_char.append(s)
    elif s == ')':
        if not last_char or last_char[-1] != '(':
            print(0)
            exit()
        if stack and stack[-1] not in target:
            tmp = []
            while stack and stack[-1] not in target:
                tmp.append(stack.pop())
            if not stack or stack[-1] != '(':
                print(0)
                exit()
            stack.pop()
            stack.append(sum(tmp) * 2)
        else:
            stack.pop()
            stack.append(2)
        last_char.pop()
    elif s == ']':
        if not last_char or last_char[-1] != '[':
            print(0)
            exit()
        if stack and stack[-1] not in target:
            tmp = []
            while stack and stack[-1] not in target:
                tmp.append(stack.pop())
            if not stack or stack[-1] != '[':
                print(0)
                exit()
            stack.pop()
            stack.append(sum(tmp) * 3)
        else:
            stack.pop()
            stack.append(3)
        last_char.pop()

for s in stack:
    if s in target:
        print(0)
        exit()

print(sum(stack))
