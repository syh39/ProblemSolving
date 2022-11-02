# 2. 코드 구현력

n = int(input())
a = []
a = list(map(int, input().split()))

consecutive = 0
ans = 0
for i in a:
    if i == 1:
        consecutive += 1
        ans += consecutive
    elif i == 0:
        consecutive = 0
print(ans)