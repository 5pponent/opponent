n, m, l = map(int, input().split())
array = list(map(int, input().split()))

array.append(0)
array.append(l-1)
array.sort()

start = 0
end = array[-1]
while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for i in range(1, len(array)):
        if array[i] - array[i-1] > mid:
            cnt += (array[i] - array[i-1] - 1) // mid

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid