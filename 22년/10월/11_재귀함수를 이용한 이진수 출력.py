# 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초

def DFS(n):
    if n > 0 :
        DFS(n//2)
        print(n%2, end='')
    else :
        return

n = int(input())
DFS(n)