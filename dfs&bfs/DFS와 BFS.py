from collections import deque

n, m, start = map(int, input().split())
graph = [ [] for _ in range(n+1) ]
visited = [False] * (n + 1)
dli = []
bli = []

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in range(len(graph)):
    graph[i] = sorted(graph[i])

def dfs(cur):
    visited[cur] = True
    dli.append(cur)
    for i in graph[cur]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur = queue.popleft()
        bli.append(cur)
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(start)
visited = [False] * (n + 1)
bfs(start)

for i in range(len(dli)):
    if i == len(dli)-1:
        print(dli[i])
    else:
        print(dli[i], end=" ")

for i in range(len(bli)):
    print(bli[i], end=" ")