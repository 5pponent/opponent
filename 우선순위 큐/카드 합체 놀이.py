import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
h = []
for i in range(n):
    heapq.heappush(h, arr[i])

for _ in range(m):
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    tmp = a + b
    heapq.heappush(h, tmp)
    heapq.heappush(h, tmp)

print(sum(h))