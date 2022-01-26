n = int(input())
for _ in range(n):
    str = list(input())
    temp = []
    for i in range(len(str)):
        if str[i] not in temp:
            temp.append(str[i])
            continue
        if str[i] in temp and i > 0 and str[i-1] != str[i]:
            n -= 1
            break
print(n)