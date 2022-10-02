def solution(stones, k):
    # 정답의 최소, 최대
    left, right = 1, 2000000000

    while left <= right:
        tmp = stones.copy()
        mid = (left + right) // 2
        cnt = 0  # 점프하는 다리 개수

        # 징검다리를 돌며 i(하중) - mid(가설 인원 수) <= 0 이면 cnt(점프 수) + 1
        # 아니면 cnt를 0으로 초기화
        for i in tmp:
            if i - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break

        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left