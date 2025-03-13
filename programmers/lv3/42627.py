import heapq


def solution(jobs):
    answer = 0
    result = 0

    jobs.sort()

    queue = []
    second = 0
    idx = 0
    cnt = 0

    while cnt < len(jobs):

        while idx < len(jobs) and jobs[idx][0] <= second:
            heapq.heappush(queue, (jobs[idx][1], jobs[idx][0]))
            idx += 1

        if queue:
            duration, request_time = heapq.heappop(queue)
            second += duration
            result += second - request_time
            cnt += 1
        else:
            second = jobs[idx][0]

    answer = result // len(jobs)

    return answer
