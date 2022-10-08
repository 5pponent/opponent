# 중요도가 가장 낮은 문서부터 출력

n = int(input())

for i in range(n):
    l, idx = map(int, input().split())
    q = list(map(int, input().split()))
    q = [[i, q[i]] for i in range(l)]
    pList = []
    print(q)

    while q:
        if q[0][1] == min(q):
            pList.append(q.pop(0))
        else:
            q.append(q.pop(0))

    print(pList)
    print(q)
