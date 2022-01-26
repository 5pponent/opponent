n = int(input())
flag = 0
a = n // 5
while True:
    temp = n
    temp -= 5 * a
    if temp % 3 != 0:
        if a - 1 < 0:
            flag = 1
            break
        a -= 1
    else:
        break
b = (n - 5 * a) // 3
if flag == 1:
    print(-1)
else:
    print(a+b)