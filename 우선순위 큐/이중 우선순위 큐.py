import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    h = []
    for _ in range(int(input())):
        cmd, val = input().split()
        if cmd == 'I':
            val = int(val)
            heapq.heappush(h, val)
        if cmd == 'D':
            if not h:
                continue
            if val == '-1':
                heapq.heappop(h)
            elif val == '1':

    if h:
        print('{} {}'.format(max(h), min(h)))
    else:
        print("EMPTY")