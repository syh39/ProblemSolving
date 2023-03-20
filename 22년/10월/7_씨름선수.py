# 4. 이분탐색(결정알고리즘) & 그리디 알고리즘

n = int(input())
body = []
for i in range(n):
    a,b = map(int, input().split())
    body.append((a,b))
body.sort(reverse=True)
largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        largest = y
        cnt+=1
print(cnt)    


