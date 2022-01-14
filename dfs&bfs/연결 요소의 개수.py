from collections import deque

노드개수, 간선개수 = map(int, input().split())
result = 0

# 빈 그래프 그리기
graph = [ [] for i in range(노드개수+1) ]
for i in range(간선개수):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (노드개수 + 1)

def 너비우선탐색(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for i in range(노드개수):
    if not visited[i+1]:
        너비우선탐색(graph, i+1, visited)
        result += 1

print(result)

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""