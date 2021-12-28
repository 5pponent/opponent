def solution(left, right):
    answer = 0

    for num in range(left, right+1):

        if num == 1:
            cnt = 1
        else:
            cnt = 2

        for i in range(2, num//2 + 1):
            if num % i == 0:
                cnt += 1

        if cnt % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer

left = 13
right = 17
print(solution(left, right))