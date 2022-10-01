def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    for i in A:
        while B:
            if B.pop(0) > i:
                answer += 1
                break

    return answer