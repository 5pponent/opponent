from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
row, col = map(int, input().split())
p_graph = []; virus = []
for _ in range(row):
    p_graph.append(list(map(int, input().split())))

xlist = [i for i in range(row)]
ylist = [i for i in range(col)]
loclist = []
for i in range(row):
    for j in range(col):
        loclist.append((xlist[i], ylist[j]))
좌표조합 = list(combinations(loclist, 3))

for i in range(row):
    for j in range(col):
        if p_graph[i][j] == 2:
            virus.append((i,j))

queue = deque()
def infectProcess():
    # BFS
    for i in range(len(virus)):
        queue.append(virus[i])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                queue.append((nx, ny))

def countSafeArea():
    count = 0
    for i in range(row):
        count += graph[i].count(0)
    return count

영역리스트 = []
for i in range(len(좌표조합)):
    cflag = False
    graph = [item[:] for item in p_graph]
    for j in range(3):
        x, y = 좌표조합[i][j]
        if graph[x][y] != 0:
            cflag = True
            break
        graph[x][y] = 1
    if cflag:
        continue
    infectProcess()
    영역리스트.append(countSafeArea())
print(max(영역리스트))
