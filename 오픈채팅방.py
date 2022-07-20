def solution(record):
    users = {}
    log = []
    result = []
    for r in record:
        splited = r.split(" ")
        if len(splited) == 3:
            users[splited[1]] = splited[2]
        log.append([splited[0], splited[1]])
    
    for cmd, uid in log:
        if cmd == "Enter":
            result.append(users[uid]+"님이 들어왔습니다.")
        if cmd == "Leave":
            result.append(users[uid]+"님이 나갔습니다.")
            
    return result
