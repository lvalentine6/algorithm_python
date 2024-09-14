import math


def solution(m, n, startX, startY, balls):
    answer = []

    for endX, endY in balls:
        # 위
        a = math.pow(endX - startX, 2) + math.pow(endY + (n - endY) * 2 - startY, 2)
        # 아래
        b = math.pow(endX - startX, 2) + math.pow(-endY - startY, 2)
        # 오른쪽
        c = math.pow(endX + (m - endX) * 2 - startX, 2) + math.pow(endY - startY, 2)
        # 왼쪽
        d = math.pow(-endX - startX, 2) + math.pow(endY - startY, 2)
        lst = [a, b, c, d]

        if startX == endX and startY > endY:
            lst.remove(b)
        elif startX == endX and startY < endY:
            lst.remove(a)
        elif startX > endX and startY == endY:
            lst.remove(d)
        elif startX < endX and startY == endY:
            lst.remove(c)

        answer.append(int(min(lst)))

    return answer
