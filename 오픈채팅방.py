import heapq
from collections import deque

def solution(jobs):
    length = len(jobs)
    cur_time = -1
    job_time = 0
    result = []
    q = []
    i = 0
    while i < length:
        if q:
            f, s = heapq.heappop(q)

            #일을 하는 동안에 일어나는 일 처리
            while True:
                if job_time == f:
                    i += 1
                    job_time = 0
                    result.append(cur_time - s)
                    break
                cur_time += 1
                job_time += 1
                for j in jobs:
                    if j[0] == cur_time:
                        new_s, new_f = j[0], j[1]
                        heapq.heappush(q, (new_f, new_s))
        else:
            cur_time += 1
            for j in jobs:
                if j[0] == cur_time:
                    new_s, new_f = j[0], j[1]
                    heapq.heappush(q, (new_f, new_s))

    return sum(result)//length
