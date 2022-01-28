for _ in range(int(input())):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())))

    result = 0
    for i in range(n):
        for j in range(m):
            if A[i] > B[j]:
                result += 1
            else:
                break
    print(result)