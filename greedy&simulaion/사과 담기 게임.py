n, m = map(int, input().split())
screen = list()
for i in range(n):
    screen.append(i+1)

c = int(input())

fall = list()
for i in range(c):
    fall.append(int(input()))

bucket = list()
for i in range(m):
    bucket.append(i+1)

result = 0

# 사과의 개수만큼 반복
for i in range(c):
    # 바구니가 사과가 떨어지는 위치에 없는 동안

    while fall[i] not in bucket:
        # 한 칸 우측으로 이동
        if bucket[len(bucket) - 1] < fall[i]:
            result += 1
            for j in range(m):
                bucket[j] += 1

        # 한 칸 좌측으로 이동
        elif bucket[0] > fall[i]:
            result += 1
            for j in range(m):
                bucket[j] -= 1

print(result)