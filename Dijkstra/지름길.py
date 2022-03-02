import sys
input = sys.stdin.readline

n, d = map(int, input().split())
distance = [ i for i in range(10001) ]
graph = [[] for i in range(10001)]

for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(d + 1):
    if i != 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    if graph[i]:
        for goal, cost in graph[i]:
            if goal <= d:
                distance[goal] = min(distance[goal], distance[i] + cost)

print(distance[d])

'''
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90
'''