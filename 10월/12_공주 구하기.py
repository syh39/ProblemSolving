# 자료구조 활용 (스택, 큐, 해쉬, 힙)

from collections import deque
n, k = map(int, input().split())
a = [i for i in range(1, n+1)]
# a = list(range(1, n+1))
a = deque(a)

while a:
    for i in range(k-1):
        a.append(a[0])
        a.popleft()
    a.popleft()
    if len(a)==1:
        print(a[0])
        a.popleft()