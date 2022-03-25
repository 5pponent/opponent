n = int(input())
arr = list(map(int,input().split()))
real = sorted(list(set(arr)))

dic = {};i = 0
for cur in real:
    dic[cur] = i
    i += 1

print(dic)

for cur in arr:
    print(dic[cur], end=' ')