def solution(numbers):
    numbers = list(map(str, numbers))
    sorted = sorted(numbers, key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(sorted)))
    return answer
