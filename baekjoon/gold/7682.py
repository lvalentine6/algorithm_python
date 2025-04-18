import sys


def check(board):
    ot = ['O', 'O', 'O']
    xt = ['X', 'X', 'X']
    for cr in range(3):
        tmp = []
        for cc in range(3):
            tmp.append(board[cr][cc])
        if tmp == ot or tmp == xt:
            return True

    for cc in range(3):
        tmp = []
        for cr in range(3):
            tmp.append(board[cr][cc])
        if tmp == ot or tmp == xt:
            return True

    if board[0][0] + board[1][1] + board[2][2] == 'OOO' or board[0][0] + board[1][1] + board[2][2] == 'XXX':
        return True
    elif board[2][0] + board[1][1] + board[0][2] == 'OOO' or board[2][0] + board[1][1] + board[0][2] == 'XXX':
        return True

    flag = False
    for b in board:
        if '.' in b:
            flag = True
            break

    if not flag:
        return True

    return False


def recursion(board, p):
    if check(board):
        target.add(''.join(''.join(b) for b in board))
        return

    for nr in range(3):
        for nc in range(3):
            if board[nr][nc] == '.':
                board[nr][nc] = p
                recursion(board, 'O' if p == 'X' else 'X')
                board[nr][nc] = '.'


input = sys.stdin.readline
lst = []

while True:
    line = input().strip()
    if line == 'end':
        break
    lst.append(line)

global target
target = set()

target_board = [['.', '.', '.'] for _ in range(3)]
recursion(target_board, 'X')

for l in lst:
    if l in target:
        print("valid")
    else:
        print('invalid')
