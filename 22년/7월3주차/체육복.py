def solution(n, lost, reserve):
    for i in reserve:
        if i in lost:
            reserve.remove(i)
            lost.remove(i) # reserve 기준 중복값 제거
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i) # lost 기준 중복값 제거
    
    reserve.sort() # reserve 정렬
    lost.sort() # lost 정렬
    
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1) # 앞사람 먼저 찾기
        elif i + 1 in lost:
            lost.remove(i + 1) # 뒤사람 찾기
    return n - len(lost)