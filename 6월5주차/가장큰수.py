num = ['19', '11', '2', '3']

print(list(map(int, num)))


def solution(numbers):
    numbers = list(map(str, numbers))
    answer = str(
        int(''.join(sorted(numbers, key=lambda x: x*3, reverse=True))))
    return answer
