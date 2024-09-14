def solution(n, arr1, arr2):
    answer = []

    lst1 = convert(n, arr1)
    lst2 = convert(n, arr2)

    for bin1, bin2 in zip(lst1, lst2):
        str = ''
        for b1, b2 in zip(bin1, bin2):
            str += '#' if b1 == '1' or b2 == '1' else ' '
        answer.append(str)

    return answer


def convert(n, arr):
    return [format(num, '0{}b'.format(n)) for num in arr]
