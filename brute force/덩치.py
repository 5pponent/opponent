n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
result = ''

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j: continue
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            rank += 1
    li[i].append(rank)
for i in range(n):
    print(li[i][2], end=" ")