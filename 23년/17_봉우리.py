n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        l1 = 0
        r1 = 0
        t1 = 0
        b1 = 0
        if i!=0:
            l1 = a[i-1][j]
        if j!=0: 
            t1 = a[i][j-1]
        if i != n-1 :
            r1 = a[i+1][j]
        if j != n-1:
            b1 = a[i][j+1]
        
        if a[i][j] > l1 and a[i][j] > r1 and a[i][j] > t1 and a[i][j] > b1:
            count += 1

print(count)
