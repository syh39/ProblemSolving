
a = [ list(map(int, input().split())) for _ in range(7)]


count = 0

for i in range(7):
    for j in range(3):
        if a[i][j] == a[i][j+4] and a[i][j+1] == a[i][j+3]:
            count += 1
        if a[j][i] == a[j+4][i] and a[j+1][i] == a[j+3][i]:
            count += 1


print(count)