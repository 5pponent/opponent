# 0: type / 5: degree
# type 1:딜, 2:힐 / degree: 딜/힐량

def solution(board, skill):
    answer = 0

    # board의 행+1 열+1 크기의 빈 2차원 배열 생성(누적합 계산용)
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    # skill 순회하며 누적합 기록
    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    # 행 별 누적합 계산
    for r in range(len(tmp) - 1):
        for c in range(len(tmp[0]) - 1):
            tmp[r][c + 1] += tmp[r][c]

    # 열 별 누적합 계산
    for c in range(len(tmp[0]) - 1):
        for r in range(len(tmp) - 1):
            tmp[r + 1][c] += tmp[r][c]

    # board에 누적합 한 번에 계산, 파괴되지 않은 건물 개수 카운트
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += tmp[r][c]
            if board[r][c] > 0: answer += 1

    return answer