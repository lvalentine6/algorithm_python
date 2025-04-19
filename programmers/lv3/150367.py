def search(tree):
    if len(tree) == 1:
        return True

    mid = len(tree) // 2
    root = tree[mid]

    left = tree[:mid]
    right = tree[mid + 1:]

    if root == '0' and ('1' in left or '1' in right):
        return False

    return search(left) and search(right)


def solution(numbers):
    answer = []

    for n in numbers:
        bi = format(n, 'b')
        l = len(bi)

        i = 0
        while 2 ** i - 1 < l:
            i += 1

        min_size = 2 ** i - 1

        padded_bi = bi.zfill(min_size)

        if search(padded_bi):
            answer.append(1)
        else:
            answer.append(0)

    return answer
