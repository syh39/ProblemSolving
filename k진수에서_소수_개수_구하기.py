import math

def conversion(n, k):
    result = ""
    while n:
        result = str(n%k) + result
        n = n//k
    return result

def isPrime(target):
    target = int(target)
    
    if target < 2:
        return False
    
    for n in range(2, int(math.sqrt(target))+1):
        if target % n == 0:
            return False
    return True
    

def solution(n, k):
    answer = 0
    if n < 2:
        return 0
    target = conversion(n, k)
    for offset in range(1, len(target)+1):
        idx = 0
        while idx+offset <= len(target):
            if "0" not in target[idx:idx+offset] and isPrime(target[idx:idx+offset]):
                if idx == 0 and idx+offset < len(target) and target[idx+offset] == "0":
                    answer += 1
                elif idx-1>=0 and target[idx-1] == "0" and idx+offset < len(target) and target[idx+offset] == "0":
                    answer += 1
                elif idx-1>=0 and target[idx-1] == '0' and idx+offset == len(target):
                    answer += 1
                elif idx == 0 and idx+offset == len(target):
                    answer += 1
                    

            idx += 1
            
    return answer
