import math

'''
 offset: 맨 앞으로 있는 숫자를 기준으로 나누어주는 변수
 k: 찾고자 하는 index
'''

def solution(n, k):
    answer = []
    arr = list(range(1, n+1))
    
    while n != 0:
        offset = math.factorial(n-1)
        index = (k-1)//offset

        answer.append(arr.pop(index))
        
        k = offset if k%offset==0 else k%offset 
        n -= 1
        
    return answer
