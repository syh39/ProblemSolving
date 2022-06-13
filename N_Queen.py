global answer

def check(result, cur_y, x):
    for (row, col) in result:
        if col == x or abs(cur_y-row) == abs(x-col):
            return False
    return True

def queen(n, cur_y, result):
    global answer

    if cur_y == n:
        answer += 1
        return
    
    for x in range(n):
        if check(result, cur_y, x): #important
            result.append((cur_y, x))
            queen(n, cur_y+1, result[:])
            result.pop()  #important 
    
def solution(n):
    global answer
    answer = 0

    queen(n, 0, [])
        
    return answer
