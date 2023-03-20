# 1 차원 리스트 생성
a=[0]*3
print(a)

a=[[0]*3 for _ in range(3)]
print(a)
a[0][1] = 1
a[2][1] = 1
print(a)
print(a[0][1])

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()