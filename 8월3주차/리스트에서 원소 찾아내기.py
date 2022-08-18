def solution(L, x):
    answer = []
    a = 5
    if x in L:
        while True:
            if x not in L:
                break

            else:
                a = L.index(x)
                L = L[a+1:]
                if len(answer) != 0:
                    a = a + answer[len(answer)-1] + 1
                answer.append(a)
    else:
        answer = [-1]
    return answer
