def solution(absolutes, signs):
    length = len(absolutes)
    answer = 0
    for i in range(0, length):
        if(signs[i]):
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
