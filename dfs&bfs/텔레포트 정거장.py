from collections import deque
import sys
input = sys.stdin.readline
맵크기, 정거장수 = map(int, input().split())
시작지점, 목표지점 = map(int, input().split())

연결정보 = [], 입구좌표 = []
for i in range(정거장수):
    x, y = map(int, input().split())
    연결정보.append((x, y))

visited = [0] * (맵크기 + 1)

def bfs():
    while lq:
        loc = lq.popleft()
        visited[loc] = count
        left = loc - 1
        right = loc + 1
        if left >= 1 and visited[left] == 0:
            result.append(left)
            visited[left] = count
        if right < 맵크기+1 and visited[right] == 0:
            result.append(right)
            visited[right] = count
        for i in range(len(연결정보)):
            if loc in 연결정보[i]:
                if loc == 연결정보[i][0] and visited[연결정보[i][1]] == 0:
                    result.append(연결정보[i][1])
                    visited[연결정보[i][1]] = count
                if loc == 연결정보[i][1] and visited[연결정보[i][0]] == 0:
                    result.append(연결정보[i][0])
                    visited[연결정보[i][0]] = count

count = 0
lq = deque(); result = deque()
lq.append(시작지점)

while 목표지점 not in result:
    count += 1
    bfs()
    if visited[목표지점] != 0:
        print(count)
        break
    for i in range(len(result)):
        lq.append(result.popleft())