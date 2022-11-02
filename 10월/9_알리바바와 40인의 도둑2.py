# DP (Top-down)

def DFS(i, j):
    if dy[i][j] > 0:
        return dy[i][j]
    else :
        dy[i][j] = min(DFS(i-1, j), DFS(i, j-1)) + arr[i][j]
        return dy[i][j]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)] 
dy[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(1, n):
        dy[0][j] = dy[0][j-1] + arr[0][j]
        dy[i][0] = dy[i-1][0] + arr[i][0]

print(DFS(n-1, n-1))