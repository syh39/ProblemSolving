# DP
# 복잡한 문제를 작은 단위의 문제로 바꾸기
# 직관적으로 답을 구함ㄹ
# 답을 메모 -> 다른 더 큰 문제 풀기

n = int(input())
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-1]+dy[i-2]
print(dy[n])