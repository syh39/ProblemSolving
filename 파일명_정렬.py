def split(s):
    list_str = list(s.upper())
    header, number = "", ""
    while True:
        if list_str[0].isdigit():
            break
        header += list_str.pop(0)
    
    while True:
        if list_str == [] or not list_str[0].isdigit():
            break
        number += list_str.pop(0)
    
    return (header, int(number), s)

def solution(files):
    result = [split(f) for f in files]
    result.sort(key=lambda x: (x[0], x[1]))
    return [r[2] for r in result]
