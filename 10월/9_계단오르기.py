# DP Bottom-up 방식

def DFS(x):
    if arr[x]>0:
        return arr[x] 
    if x == 1 or x == 2 :
        return x
    else :
        arr[x] = DFS(x-1) + DFS(x-2)
        return arr[x]
    

n = int(input())
arr = [0]*(n+2)
arr[1] = 1
arr[2] = 2
for i in range(3, n+2):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[n+1])