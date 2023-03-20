# 구현
N = int(input())

a = list(map(int, input().split()))
avg = int(round(sum(a)/N))

min = a[0] # 가장 적은 차이
closestIdx = 0 # 가장 가까운 숫자
for idx, i in enumerate(a):
    dif = abs(avg-i)
    if dif<min:
        min = dif
        closestIdx = idx
    elif dif==min:
        if a[closestIdx] < a[idx] :
            closestIdx = idx
            
print(avg, closestIdx+1)
print(round(4.5))
