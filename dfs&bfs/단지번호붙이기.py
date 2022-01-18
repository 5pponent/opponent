import copy
def dfs(x, y):
    global total
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        ginfo[x][y] = total + 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
ginfo = copy.deepcopy(graph)
total = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            total += 1
print(total)

result = [0 for i in range(total)]
for i in range(n):
    for j in range(1, total+1):
        result[j-1] += ginfo[i].count(j)
result.sort()
print("\n".join(str(i) for i in result))
