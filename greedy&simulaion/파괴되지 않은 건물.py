# 0: type / 5: degree
# type 1:딜, 2:힐 / degree: 딜/힐량

def solution(board, skill):
    # skill 순회
    for each in skill:
        print(each[1], each[3], each[2], each[4])
        for r in range(each[1], each[3] + 1):
            for c in range(each[2], each[4] + 1):
                if (each[0] == 1): 
                    board[r][c] -= each[5]
                else:
                    board[r][c] += each[5]

    # 남은 건물 개수
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if (board[r][c] > 0): answer += 1

    return answer