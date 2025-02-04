def check(stones, k, mid):
    cnt = 0

    for stone in stones:
        if stone < mid:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0

    return True


def solution(stones, k):
    answer = 0

    left = 1
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2

        if check(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1

    answer = right

    return answer
