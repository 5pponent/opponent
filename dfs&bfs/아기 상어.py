import gc
from collections import deque
import sys
input = sys.stdin.readline

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.크기 = 2
        self.먹은횟수 = 0

    def 물고기먹기(self, x, y):
        graph[아기상어.x][아기상어.y] = 0
        graph[x][y] = 9
        아기상어.x = x
        아기상어.y = y
        아기상어.먹은횟수 += 1
        if 아기상어.크기 == 아기상어.먹은횟수:
            아기상어.크기 += 1
            아기상어.먹은횟수 = 0

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            아기상어 = Fish(i, j)

def bfs():
    global result
    q = deque()
    q.append(아기상어.x)
    q.append(아기상어.y)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[아기상어.x][아기상어.y] = 1

    while q:
        x = q.popleft()
        y = q.popleft()

        for nx, ny in [[x-1, y], [x, y-1], [x, y+1], [x+1, y]]:
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > 아기상어.크기:
                continue
            if graph[nx][ny] < 아기상어.크기:
                if graph[nx][ny] != 0:
                    아기상어.물고기먹기(nx, ny)
                    result += visited[x][y]
                    for i in range(n):
                        print(graph[i], end="  ");print(visited[i])
                    print()
                    return True
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append(nx)
                q.append(ny)
    return False

def printInfo():
    print("아기상어 : {},{} / 크기 : {} / 먹은횟수 : {}"
          .format(아기상어.x, 아기상어.y, 아기상어.크기, 아기상어.먹은횟수))
    print(result)
    print()

result = 0
while True:
    if not bfs():
        break
    gc.collect()
    printInfo()
print(result)