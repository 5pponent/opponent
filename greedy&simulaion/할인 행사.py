def solution(want, number, discount):
    answer = 0

    li = []
    for i in range(len(want)):
        for j in range(number[i]):
            li.append(want[i])
    li = sorted(li)

    for i in range(len(discount) - 9):
        if li == sorted(discount[i:i + 10]):
            answer += 1

    return answer