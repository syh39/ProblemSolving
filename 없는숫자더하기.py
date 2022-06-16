def solution(numbers):
    answer = 0
    index = 0
    numbers.sort()
    tempList = [0 for i in range(10)]
    for i in numbers :
        tempList[i] = 1
    for i in tempList:
        if i == 0 :
            answer += index
        index += 1
    return answer