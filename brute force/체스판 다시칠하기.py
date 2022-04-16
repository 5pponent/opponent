m, n = map(int, input().split())
g = []
for _ in range(m):
    g.append(list(input()))
for i in range(m):
    for j in range(n):
        if g[i][j] == 'B': g[i][j] = 1
        elif g[i][j] == 'W': g[i][j] = -1

res = 2500
for x in range(m-7):
    for y in range(n-7):
        temp = []
        for i in range(8):
            temp.append(g[x + i][y:y + 8])

        for _ in range(2):
            if temp[0][0] == 1: temp[0][0] = -1
            else: temp[0][0] = 1

            sum = 0
            for i in range(1, 8):
                if temp[0][i-1] == temp[0][i]:
                    if temp[0][i-1] == 1: temp[0][i] = -1
                    else: temp[0][i] = 1
                    sum += 1

            for i in range(8):
                tmp = 0
                for j in range(8):
                    tmp += temp[i][j]
                sum += abs(tmp) // 2
            res = min(res, sum)
print(res)