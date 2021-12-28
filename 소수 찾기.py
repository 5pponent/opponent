def solution(numbers):
    answer = 0
    numbers = list(numbers)

    for i in range(0, len(numbers)):
        if isPrimeNumber(i): answer += 1; print(i)

        for j in range(0, len(numbers)):
            if i == j: continue
            num = int(numbers[i]+numbers[j])
            if isPrimeNumber(num): answer += 1; print(num)

            for k in range(1, num+1):
                n=1

    return answer

def isPrimeNumber(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(solution("011"))