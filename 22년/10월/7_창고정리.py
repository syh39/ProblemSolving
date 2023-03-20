# 4. 이분탐색(결정알고리즘) & 그리디 알고리즘

L = int(input())
a = list(map(int, input().split()))
M = int(input())

a.sort()
for i in range(M):
    a[-1] -= 1
    a[0] += 1
    a.sort()

print(a[-1]-a[0])