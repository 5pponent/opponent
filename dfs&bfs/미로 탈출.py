from collections import deque

행, 열 = map(int, input().split())
미로 = []
for i in range(행):
    미로.append(list(map(int, input())))

# 이동 가능한 4방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def 미로찾기(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 행 or ny < 0 or ny >= 열:
                continue
            if 미로[nx][ny] == 0:
                continue
            if 미로[nx][ny] == 1:
                미로[nx][ny] = 미로[x][y] + 1
                queue.append((nx, ny))

    return 미로[행-1][열-1]

print(미로찾기(0,0))

for i in range(행):
    print(미로[i])