# 자료구조 활용 (스택, 큐, 해쉬, 힙)

# n, l = map(int, input().split())
# n = [int(x) for x in str(n)]
# temp = []
# length = len(n)-l
# print(length)


# for i in range(len(n)):
#     while True:
#         if len(temp)==0:
#             temp.append(n[0])
#             n.pop(0)
#             print('1', temp, n, l)
#             break
#         elif temp[-1] >= n[0] or l==0:
#             if len(temp) < length:
#                 temp.append(n[0])
#                 n.pop(0)
#                 print('2', temp, n, l)
#                 break
#             else :
#                 n.pop(0)
#                 break
#         if l > 0:
#             temp.pop()
#             l-=1
#         print('3', temp, n, l)

# for i in temp:
#     print(i, end='')

# 자료구조 활용 (스택, 큐, 해쉬, 힙)

# n, l = map(int, input().split())
# n = [int(x) for x in str(n)]
# temp = []
# length = len(n)-l

# for i in range(len(n)):
#     while True:
#         if len(temp)==0:
#             temp.append(n[0])
#             n.pop(0)
#             break
#         elif temp[-1] >= n[0] or l==0:
#             if len(temp) < length:
#                 temp.append(n[0])
#                 n.pop(0)
#                 break
#             else :
#                 n.pop(0)
#                 break
#         if l > 0:
#             temp.pop()
#             l-=1

# for i in temp:
#     print(i, end='')

num, m = map(int, input().split())
num=list(map(int, str(num)))
stack=[]

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m!=0:
    stack=stack[:-m]

res=''.join(map(str,stack))
print(res)
# for i in stack:
#     print(i, end="")

