def solution(citations):
    answer = []
    citations.sort()
    for h in range(len(citations)+1):
        tmp = 0
        if citations[0] > h:
            continue
        for c in citations:
            if c >= h:
                tmp += 1
                
        if tmp >= h:
            answer.append(h)
            
    return sorted(answer).pop()
