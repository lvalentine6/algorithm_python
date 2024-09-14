import math


def solution(n, k):
    answer = 0;
    n = int(n)
    k = int(k)

    result = ''
    while n > 0:
        remain = n % k
        result = str(remain) + result
        n //= k

    sp_lst = result.split('0')
    result_lst = [int(i) for i in sp_lst if i != '1' and i != '']

    for r in result_lst:
        flag = False
        for i in range(2, int(math.sqrt(r)) + 1):
            if r % i == 0:
                flag = True
                break
        if not flag:
            answer += 1

    return answer
