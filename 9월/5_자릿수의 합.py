def digit_sum(x):
    res = 0
    # for i in str(x):
    #     res += int(i)
    while x>0 :
        tmp = x%10
        res += tmp
        x = x//10
    return res

N = int(input())
a = list(map(int, input().split()))
# res = []

maxSum = 0
for i in a:
    sumDigit = digit_sum(i)
    if sumDigit > maxSum:
        maxSum = sumDigit
        res = i
print(i)
    
#     res.append(sumDigit)

# for idx, i in enumerate(res):
#     if i == maxSum:
#         print(a[idx])
#         break


