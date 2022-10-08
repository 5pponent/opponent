n = int(input())
rope = sorted([ int(input()) for i in range(n) ])
ws = 0

for _ in range(n):
    w = sum(rope) // len(rope)
    if rope[0] < w:
        ws = max(rope[0] * len(rope), ws)
    else:
        ws = max((w * len(rope)), ws)
    rope.pop(0)

print(ws)