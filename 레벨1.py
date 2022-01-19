def solution1(n):
    answer = int(''.join(sorted(str(n), reverse=True)))
    return answer

def solution2(price, money, count):
    total = 0
    for i in range(count):
        total += price * (i + 1)
    if money - total > 0:
        return 0
    return abs(money - total)
