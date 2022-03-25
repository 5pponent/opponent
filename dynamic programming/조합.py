n, r = map(int, input().split())
d = [[0] * 101 for i in range(101)]

def combi(a,b):
    if b == 1:
        return a
    if a == b:
        return 1
    if d[a][b] != 0:
        return d[a][b]
    d[a][b] = combi(a-1, b-1) + combi(a-1, b)
    return d[a][b]

print(combi(n,r))