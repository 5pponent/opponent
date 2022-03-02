from collections import deque

gear = []
action = deque()

for _ in range(4):
    gear.append(list(map(int, input())))
for i in range(int(input())):
    action.append(tuple(map(int, input().split())))

def rotate(target, dir):
    if dir == -1:
        temp = gear[target].pop(0)
        gear[target].append(temp)
    elif dir == 1:
        temp = gear[target].pop()
        gear[target].insert(0, temp)

while action:
    target, direction = action.popleft()
    target -= 1
    toRotate = [False] * 4
    toRotate[target] = True

    # 왼쪽으로 비교
    cur = target
    while True:
        if cur == 0: break
        if gear[cur][6] != gear[cur-1][2]:
            toRotate[cur-1] = True
        else: break
        cur -= 1
    # 오른쪽으로 비교
    cur = target
    while True:
        if cur == 3: break
        if gear[cur][2] != gear[cur+1][6]:
            toRotate[cur+1] = True
        else: break
        cur += 1

    rotate(target, direction)
    # 왼쪽으로 회전
    cur = target - 1
    oldMove = direction
    while cur >= 0:
        if toRotate[cur] == True:
            rotate(cur, (oldMove * -1))
            oldMove *= -1
        else: break
        cur -= 1
    # 오른쪽으로 회전
    cur = target + 1
    oldMove = direction
    while cur <= 3:
        if toRotate[cur] == True:
            rotate(cur, (oldMove * -1))
            oldMove *= -1
        else: break
        cur += 1

result = 0
if gear[0][0] == 1: result += 1
if gear[1][0] == 1: result += 2
if gear[2][0] == 1: result += 4
if gear[3][0] == 1: result += 8
print(result)