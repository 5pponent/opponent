n, l = map(int, input().split())
arr = sorted(list(map(int,input().split())))

result = 1

try:
    i = 0
    while i < len(arr):
        for j in range(1,l+1):
            if arr[i+j] - arr[i] >= l:
                i = i + j
                result += 1
                break
except:
    pass

print(result)