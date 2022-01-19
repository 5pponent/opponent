from itertools import combinations
from collections import deque
import time

col, row = map(int, input().split())
graph = []
for i in range(col):
    graph.append(list(map(int, input().split())))

# 벽이 없는 좌표를 가져온다
empty = []
for i in range(col):
    for j in range(row):
        if graph[i][j] == 0:
            empty.append((i, j))

# 3개의 벽을 둘 조합을 모두 구한다
wall_case = combinations(empty, 3)


# 3개의 벽의 좌표를 전달받아서 벽을 세운 그래프를 돌려주는 함수
def make_copy(three_walls):
    graph_copy = [item[:] for item in graph]

    for coord in three_walls:
        x, y = coord
        graph_copy[x][y] = 1
    return graph_copy


def bfs(g):
    global escape
    for i in range(len(temp_q)):
        q.append(temp_q.popleft())
    if not temp_q and not q:
        escape = True
        return

    while q:
        x, y = q.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if g[nx][ny] == 2 or g[nx][ny] == 1:
                continue
            if g[nx][ny] == 0:
                g[nx][ny] = 2
                # 본 큐에 넣는게 아닌, 임시 큐에 넣는다
                temp_q.append((nx, ny))


# 바이러스를 찾아서 메인 큐에 집어넣기
init_virus = []
for i in range(col):
    if 2 in graph[i]:
        for j in range(row):
            if graph[i][j] == 2:
                init_virus.append((i, j))


def put_init_virus(g):
    for virus_coord in init_virus:
        x, y = virus_coord
        g[x][y] = 2


# case : ((6, 4), (6, 5), (6, 6))
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for case in wall_case:
    # 기본 세팅
    q = deque()
    temp_q = deque()
    escape = False
    g = make_copy(case)
    count = 0
    put_init_virus(g)

    while not escape:  # 메인 루프
        bfs(g)
        for i in range(row):
            for j in range(col):
                print(g[i][j], end=" ")
            print()
        print()
        time.sleep(2)
        count += 1

    result.append(count)

print(max(result))