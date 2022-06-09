def validation(p):
    stack = []
    
    for s in p:
        if s == "(":
            stack.append(s)
        else:
            if stack == [] and s == ")":
                return False
            else:
                stack.pop()
    return stack == []

def reversed_para(p):
    return "".join(["(" if s ==")" else ")" for s in p ])

def recursion(p):
    if p == "":
        return ""
    u, v = "", ""
    zero_sum = 0
    for s in p:
        if zero_sum == 0 and u != "":
            break
        if s == "(":
            zero_sum += 1
        elif s == ")":
            zero_sum -= 1
        u += s
    v = p.replace(u, "", 1)
    
    if validation(u):
        return u + recursion(v)
    else:
        return "(" + recursion(v) + ")" + reversed_para(u)[1:-1]
    
def solution(p):
    if p == "" or validation(p):
        return p
    
    return recursion(p)
