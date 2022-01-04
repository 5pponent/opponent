# 300초  5분
# 60초   1분
# 10초
def solution(T):
    if T % 10 != 0:
        return -1

    cA = T // 300
    T %= 300
    cB = T // 60
    T %= 60
    cC = T // 10

    return '{} {} {}'.format(cA, cB, cC)

t = int(input())
print(solution(t))