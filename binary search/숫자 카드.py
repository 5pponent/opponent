n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = list(map(int, input().split()))

def bsearch(ary, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if ary[mid] == target:
        return 1
    elif ary[mid] > target:
        return bsearch(ary, target, start, mid - 1)
    else:
        return bsearch(ary, target, mid + 1, end)

for i in range(m):
    print(bsearch(A, B[i], 0, n-1), end=" ")