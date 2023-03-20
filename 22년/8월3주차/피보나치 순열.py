def solution(x):
    return recursive(x)


def recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursive(n-1) + recursive(n-2)


def iterative(n):
    list = []
    for i in range(0, n+1):
        if i == 0 or i == 1:
            list.append(i)
        else:
            list.append(list[i-2] + list[i-1])
    return list[n]
