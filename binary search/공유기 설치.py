n, c = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(int(input()))
graph.sort()

start = 1
end = graph[-1] - graph[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    cur = graph[0]
    count = 1

    for i in range(1, len(graph)):
        if graph[i] >= cur + mid:
            count += 1
            cur = graph[i]
    if count >= c:  # 간격이 좁아서 공유기를 더 많이 설치했을 때
        start = mid + 1
        result = mid
    else:           # 간격이 넓어서 공유기를 다 설치하지 못했을 때
        end = mid - 1
print(result)