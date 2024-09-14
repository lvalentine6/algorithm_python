import heapq


def solution(A, B):
    min_heap = A
    heapq.heapify(min_heap)

    max_heap = [-b for b in B]
    heapq.heapify(max_heap)

    answer = sum(heapq.heappop(min_heap) * -heapq.heappop(max_heap) for _ in range(len(min_heap)))

    return answer
