def solution(n, left, right):
    answer = []

    while left <= right:
        answer.append(max(left // n, left % n) + 1)
        left += 1

    return answer