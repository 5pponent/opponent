def solution(numbers):
    answer = []

    for i in range(0,len(numbers)-1):
        for j in range(i+1, len(numbers)):
            res = numbers[i] + numbers[j]

            if res not in answer:
                answer.append(res)

    return sorted(answer)

