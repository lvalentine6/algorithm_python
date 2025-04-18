import math
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
N = int(math.pow(2, n))
cnt = 0

def recursion(size, row, col):
    global cnt
    if size == 1:
        if row == r and col == c:
            print(cnt)
            exit(0)
        cnt += 1
        return

    half = size // 2
    if r < row + half and c < col + half:
        recursion(half, row, col)
    elif r < row + half and c >= col + half:
        cnt += half * half
        recursion(half, row, col + half)
    elif r >= row + half and c < col + half:
        cnt += 2 * half * half
        recursion(half, row + half, col)
    else:
        cnt += 3 * half * half
        recursion(half, row + half, col + half)

recursion(N, 0, 0)
