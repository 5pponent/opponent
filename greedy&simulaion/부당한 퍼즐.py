import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
corr = list(map(int, input().split()))
arr = list(map(int, input().split()))

idx = arr.index(corr[0])