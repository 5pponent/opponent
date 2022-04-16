from collections import deque

n = int(input())
graph = [ [] for i in range(n+1) ]
start, end = map(int, input().split())

for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
distance = [0] * (n + 1)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                distance[next] = distance[cur] + 1
                if next == end:
                    return distance[next]
    return -1

print(BFS(graph, start, visited))