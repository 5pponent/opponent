from collections import deque
import sys
input = sys.stdin.readline

row, col = map(int, input().split())
graph = []
for _ in range(row):
    graph.append(list(input()))

백조위치 = []
for i in range(row):
    for j in range(col):
        if graph[i][j] == 'L':
            백조위치.append(i)
            백조위치.append(j)
            break

def 하루경과():
    녹을공간 = []
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 'X':
                for x, y in [[i-1, j],[i+1, j],[i, j-1],[i, j+1]]:
                    if x < 0 or x >= row or y < 0 or y >= col:
                        continue
                    if graph[x][y] == '.':
                        녹을공간.append((i,j))
                        break
    for x,y in 녹을공간:
        graph[x][y] = '.'

def 만날수있는지확인():
    q = deque()
    q.append(백조위치[0])
    q.append(백조위치[1])
    visited = [[0 for _ in range(col)] for _ in range(row)]

    while q:
        curX = q.popleft()
        curY = q.popleft()
        visited[curX][curY] = 1

        for nextX, nextY in \
                [[curX+1, curY], [curX-1, curY], [curX,curY-1], [curX,curY+1]]:
            if nextX < 0 or nextX >= row or nextY < 0 or nextY >= col:
                continue
            if graph[nextX][nextY] == 'X' or visited[nextX][nextY] == 1:
                continue
            if graph[nextX][nextY] == 'L':
                return True
            q.append(nextX)
            q.append(nextY)
    return False

result = 0
while not 만날수있는지확인():
    하루경과()
    result += 1
print(result)