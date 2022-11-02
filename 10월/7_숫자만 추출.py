# 3. 탐색 & 시뮬레이션(string, 1차원 & 2차원 리스트 탐색)

def getDivisor(x):
    cnt = 0
    for i in range(1, x+1):
        if x%i==0:
            cnt += 1
    return cnt


s = input()
num = ""
for i in s:
    if 48 <= ord(i) <= 57 :
        num += i
num = int(num)
print(num)
print(getDivisor(num))
