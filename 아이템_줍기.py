def bfs(table, characterX, characterY, itemX, itemY):

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    stack = [(characterX, characterY, 0)]
    answer = []
    
    while stack:
        cx, cy, cnt = stack.pop(0)
        
        if cx == itemX and cy == itemY:
            return cnt
        
        for x, y in zip(dx, dy):
            nx = cx + x
            ny = cy + y
            if nx > 0 and ny > 0 and table[ny][nx] == 1:
                table[ny][nx] = -1
                stack.append((nx, ny, cnt+1))

def solution(rectangle, characterX, characterY, itemX, itemY):
    table = [[0 for _ in range(150)] for _ in range(150)]
    
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        y1 *= 2
        x2 *= 2
        x1 *= 2
        y2 *= 2
        for i in range(y1, y2+1):
            if i == y1 or i == y2:
                for j in range(x1, x2+1):
                    if table[i][j] != 7:
                        table[i][j] = 1
                   
            else:
                for j in range(x1, x2+1):
                    if j == x1 or j == x2:
                        if table[i][j] != 7:
                            table[i][j] = 1
                    else:
                        table[i][j] = 7

    return bfs(table, characterX*2, characterY*2, itemX*2, itemY*2)//2
