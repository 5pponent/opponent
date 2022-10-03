from collections import deque

# 이동 가능한 4방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 9999999999


def solution(board):
    global answer
    queue = deque()
    dp = [[[answer for y in range(len(board))] for x in range(len(board))] for z in range(4)]

    for z in range(4):
        dp[z][0][0] = 0
    if board[0][1] != 1:
        queue.append([0, 1, 100, 3])
        dp[1][0][1] = 100
    if board[1][0] != 1:
        queue.append([1, 0, 100, 1])
        dp[0][1][0] = 100

    while queue:
        x, y, cost, beforeDir = queue.popleft()
        for currentDir in range(4):
            nx = x + dx[currentDir]
            ny = y + dy[currentDir]

            if beforeDir != currentDir:
                ncost = cost + 600
            else:
                ncost = cost + 100

            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[nx][ny] != 1:
                    if dp[currentDir][nx][ny] > ncost:
                        queue.append((nx, ny, ncost, currentDir))
                        dp[currentDir][nx][ny] = ncost

    for z in range(4):
        if answer > dp[z][len(board) - 1][len(board) - 1]:
            answer = dp[z][len(board) - 1][len(board) - 1]

    return answer
