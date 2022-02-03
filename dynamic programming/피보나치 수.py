from collections import deque

n = int(input())
def fibo(x):
    li = deque([0, 1])
    idx = 2
    if x < 2: return li[x]
    while idx <= x:
        temp = li.popleft()
        li.append(li[-1] + temp)
        idx += 1
    return li[-1]

print(fibo(n))