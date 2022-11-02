# 3. 탐색 & 시뮬레이션(string, 1차원 & 2차원 리스트 탐색)

n = int(input())

for i in range(n):
    ipt = input()
    ipt = ipt.upper()

    for j in range(len(ipt)//2):
        if ipt[j] != ipt[len(ipt)-1-j]:
            # ipt[j] != ipt[-1-j] 이런식으로 해도 됨
            print("#{} NO".format(i+1))
            # print("#%d NO" %(i+1)) 이렇게 해도 됨
            break
    else :
        print("#{} YES".format(i+1))

# if s == s[::-1] 더 파이썬 스럽게 하는 방법
