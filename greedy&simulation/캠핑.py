i = 0
while True:
    use, time, total = map(int, input().split())
    if use==0 and time==0 and total==0:
        break
    i += 1
    result = 0

    while total - time > 0:
        result += use
        total -= time

    if total >= use:
        result += use
    elif total < use:
        result += total
    print('Case {}: {}'.format(i, result))