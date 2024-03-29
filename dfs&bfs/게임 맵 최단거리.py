from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    answer = bfs(maps)
    return -1 if answer == 1 else answer

def bfs(maps):
    row = len(maps)
    col = len(maps[0])
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    return maps[row - 1][col - 1]