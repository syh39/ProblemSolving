from itertools import permutations
import math


def solution(numbers):
    num = [n for n in numbers]  # '17' -> ['1', '7']
    per = []

    for i in range(1, len(numbers)+1):
        per += list(permutations(num, i))  # i개씩 순열조합

    new_num = [int(('').join(p)) for p in per]  # int 형의 순열 조합
    return countPrimeNumber(set(new_num))  # 중복 제거 후 함수에 넘김


def countPrimeNumber(new_num):
    ans = 0
    for n in new_num:
        checkPrime = True
        if(n < 2):  # 2보다 더 큰 수에 한해서
            continue
        for i in range(2, int(math.sqrt(n))+1):  # 순열 구하는 방법
            if n % i == 0:
                checkPrime = False
                break
        if checkPrime:  # 소수인 경우 count++
            ans += 1
    return ans
