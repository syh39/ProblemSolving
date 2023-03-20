# DP 재귀(Top-down) + 메모이제이션

def DFS(len):
    if dy[len]>0:
        return dy[len] # 메모이제이션 리턴
    if len==1 or len==2:
        return len
    else :
        dy[len] = DFS(len-1)+DFS(len-2)
        return dy[len]

n = int(input())
dy = [0]*(n+1)
print(DFS(n))