def solution(priorities, location):
    prior = [(p, i) for i, p in enumerate(priorities)]
    cnt = 0
    
    while True:
        maximum, _ = max(prior)
        p, i = prior.pop(0)
        if p == maximum:
            cnt += 1
            if i == location:
                return cnt
        else:
            prior.append((p, i))
