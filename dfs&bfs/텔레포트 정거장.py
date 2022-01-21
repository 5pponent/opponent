from collections import deque
import sys
input = sys.stdin.readline

맵크기, 정거장수 = map(int, input().split())
시작지점, 목표지점 = map(int, input().split())

텔레포트 = [[] for _ in range(맵크기+1)]
for _ in range(정거장수):
    x, y = map(int, input().split())
    텔레포트[x].append(y)
    텔레포트[y].append(x)

visited = [0] * (맵크기 + 1)

def bfs():
    q = deque()
    q.append(시작지점)
    while q:
        cur = q.popleft()
        if cur == 목표지점:
            return visited[cur]

        이동가능위치목록 = [cur + 1, cur - 1]
        if 텔레포트[cur]:
            for i in 텔레포트[cur]:
                이동가능위치목록.append(i)

        for next in 이동가능위치목록:
            if 0 <= next <= 맵크기 and visited[next] == 0:
                visited[next] = visited[cur] + 1
                q.append(next)

print(bfs())