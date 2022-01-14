from collections import deque

# 100 이하
컴퓨터수 = int(input())
result = 0

# 빈 그래프 그리기
graph = [ [] for i in range(컴퓨터수+1) ]
for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 확인용 리스트 선언
visited = [False] * (컴퓨터수 + 1)

# 깊이우선탐색
"""
def 깊이우선탐색(graph, cur, visited):
    global result
    visited[cur] = True
    result += 1
    for i in graph[cur]:
        if not visited[i]:
            깊이우선탐색(graph, i, visited)

깊이우선탐색(graph, 1, visited)
"""

# 너비우선탐색
def 너비우선탐색(graph, start, visited):
    global result
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        result += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

너비우선탐색(graph, 1, visited)

print(result-1)

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