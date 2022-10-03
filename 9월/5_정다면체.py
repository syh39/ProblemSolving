# 구현
N, M = map(int, input().split())

cnt = [0]*500 # 정답의 개수

max = 0
for n in range(1, N+1):
    for m in range(1, M+1):
        res = n+m
        cnt[res] += 1
        if cnt[res] > max:
            max = cnt[res]

for idx, c in enumerate(cnt):
    if c == max:
        print(idx, end= ' ')

