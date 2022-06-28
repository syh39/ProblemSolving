def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(answer1(array, i))
    return answer


def answer1(array, command):
    print('answer1')
    array = array[command[0]-1:command[1]]
    array.sort()
    return array[command[2]-1]
