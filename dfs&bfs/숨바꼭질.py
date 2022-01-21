from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        cur = q.popleft()
        if cur == k:
            print(visited[cur])
            return

        for i in [cur-1, cur+1, cur*2]:
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[cur] + 1
                q.append(i)

n, k = map(int, input().split())
visited = [0] * 100001

bfs()