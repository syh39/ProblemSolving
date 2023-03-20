
def checkFunction1(arr):
    for i in range(9):
        checkArr1 = []
        checkArr2 = []
        for j in range(9):
            if arr[i][j] in checkArr1 or arr[j][i] in checkArr2:
                return False
            checkArr1.append(arr[i][j])
            checkArr2.append(arr[j][i])
          
    return True

def checkFunction2(arr):
    for i in [0,3,6]:
        for j in [0,3,6]:
            checkArr = []
            for k in range(i,i+3):
                for l in range(j, j+3):
                    if arr[k][l] in checkArr:
                        return False
                    checkArr.append(arr[k][l])
    return True


arr = [list(map(int, input().split())) for _ in range(9)]


if checkFunction1(arr) and checkFunction2(arr):
    print("YES")
else:
    print("NO")

    



