모든수 = [i for i in range(1, 10001)]

def delNotSelfNum(n):
    tmp = n
    tmp = list(str(tmp))
    sum = 0
    for i in tmp:
        sum += int(i)
    sum += n
    if sum in 모든수:
        모든수.remove(sum)

for i in range(1,10001):
    delNotSelfNum(i)
for i in range(len(모든수)):
    print(모든수[i])