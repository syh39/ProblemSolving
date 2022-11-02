# DP (Bottom-up)

n = int(input())
arr = []
dy = [[0]*n]*n
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]

# temp_list = []
# for i in range(n):
#     temp_list = list(map(int, input().split()))
#     arr.append(temp_list)

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dy[i][j] = arr[i][j]
        elif i==0 :
            dy[i][j] = dy[i][j-1] + arr[i][j]
        elif j==0:
            dy[i][j] = dy[i-1][j] + arr[i][j]
        else :
            dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]
print(dy[n-1][n-1])