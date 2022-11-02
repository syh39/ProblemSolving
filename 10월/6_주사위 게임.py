# 코드 구현력


def calculate(n, dup):
    if dup == 1 :
        return n*100
    elif dup == 2 :
        return 1000+(n*100)
    elif dup == 3 :
        return 10000 + (n*1000)

N = int(input())
a = []
ans = []
for i in range(N):
    a = (map(int, input().split()))
    n1 = a.count(a[0]) 
    n2 = a.count(a[1])
    n3 = a.count(a[2])    
    dup = max(n1, n2, n3)
    if dup == 1:
        ans.append(calculate(max(a), 1))
    else :
        if n1==dup:
            ans.append(calculate(a[0], dup))
        elif n2==dup:
            ans.append(calculate(a[1], dup))
        elif n3==dup:
            ans.append(calculate(a[2], dup))

print(max(ans))

        

        
