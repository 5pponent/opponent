from collections import deque

수빈, 동생 = map(int, input().split())

def 숨바꼭질(수빈, 동생):
    count = 0
    q = []
    sqrts = [3 ** i for i in range(10)]
    for i in range(10):
        for j in range(i):
            sqrts[i] += sqrts[j]
    queue = deque()
    queue.append(수빈)

    while queue:
        count += 1
        현위치 = queue.popleft()
        if 현위치 == 동생:
            for i in range(10):
                if count <= sqrts[i]:
                    return i
        n1 = 현위치 + 1
        n2 = 현위치 - 1
        n3 = 현위치 * 2
        queue.append(n1)
        queue.append(n2)
        queue.append(n3)

print(숨바꼭질(수빈,동생))