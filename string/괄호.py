for _ in range(int(input())):
    temp = list(input())
    stack = 0
    for i in temp:
        if i == '(':
            stack += 1
        if i == ')':
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print("YES")
    else:
        print("NO")