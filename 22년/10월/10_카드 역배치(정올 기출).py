# 탐색 & 시뮬레이션 ㅇ

# original_arr = [i for i in range(1,21)]
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)
for i in a:
    print(i, end=' ')