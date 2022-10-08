t = int(input())
for _ in range(t):
    n = int(input())
    지원자 = []
    for i in range(n):
        지원자.append(list(map(int, input().split())))
    지원자.sort(key=lambda x:x[0])
    result = 1
    idx = 0
    for i in range(1, n):
        if 지원자[i][1] > 지원자[idx][1]:
            continue
        else:
            idx = i
            result += 1
    print(result)