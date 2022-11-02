# 이분탐색(결정알고리즘) & 그리디 알고리즘 ㅇ

N, M = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

lo = 0
hi = len(a)-1
while lo<=hi:
    mid = (lo + hi)//2
    if a[mid]==M:
        print(mid+1)
        break
    elif a[mid] > M:
        hi = mid-1
    elif a[mid] < M:
        lo = mid+1
    
    

