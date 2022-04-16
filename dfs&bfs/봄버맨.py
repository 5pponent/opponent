from collections import deque

row, col, n = map(int, input().split())
graph = []; 터질것들 = deque()
for _ in range(row):
    graph.append(list(input()))

t = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
임시좌표 = []
for i in range(row):
    for j in range(col):
        if graph[i][j] == "O":
            임시좌표.append((i, j))
터질것들.append(tuple(임시좌표))

def 폭탄심기(graph):
    임시좌표 = []
    for i in range(row):
        for j in range(col):
            if graph[i][j] == ".":
                임시좌표.append((i, j))
                graph[i][j] = "O"
    터질것들.append(tuple(임시좌표))

def 터치기(q, graph):
    temp = q.popleft()
    for x, y in temp:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            if (nx, ny) not in temp and graph[nx][ny] == "O":
                graph[nx][ny] = "."
        graph[x][y] = "."

while t < n:
    t += 1
    if t == 1:
        continue
    if t % 2 == 0:
        if n == 2:
            break
        폭탄심기(graph)
    elif t % 3 == 0:
        터치기(터질것들, graph)
for i in range(row):
    for j in range(col):
        print(graph[i][j], end="")
    print()