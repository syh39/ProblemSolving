# 자료구조 활용 (스택, 큐, 해쉬, 힙)

n = input()
stack = []
stick_num = 0
stick_cut_num = 0
first = True

for i in range(len(n)):
    if n[i] == '(':
        stack.append(n[i])
    else :
        stack.pop()
        if n[i-1] == '(':
            stick_cut_num += len(stack)
        else : 
            stick_cut_num += 1
        

print(stick_cut_num)
    


        




#     print('------------------')
#     print(i)
#     print('------------------')

#     if len(stack)==0:
#         stack.append(i)
#         if i == '(':
#             stick_num += 1
#         if i == ')':
#             stick_num -= 1
#         print('1', stack, '| stick_num : ', stick_num, '| stick_cut_num : ', stick_cut_num)

#     elif stack[-1] == '(' and i== ')':
#         stick_num -=1
#         stick_cut_num += stick_num
#         stack.pop()
#         print('2', stack, '| stick_num : ', stick_num, '| stick_cut_num : ', stick_cut_num)
    
#     elif stack[-1] == '(' and i== '(':
#         stick_num +=1
#         stack.pop()
#         stack.append(i)
#         print('3', stack, '| stick_num : ', stick_num, '| stick_cut_num : ', stick_cut_num)
    
#     elif stack[-1] == ')' and i == ')':
#         stick_num -= 1
#         stack.pop()
#         stack.append(i)
#         print('4', stack, '| stick_num : ', stick_num, '| stick_cut_num : ', stick_cut_num)


# print(stick_cut_num)

        
