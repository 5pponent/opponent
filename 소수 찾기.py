from itertools import combinations, permutations

def solution(numbers):
    answer = 0
    al = []; pl = []
    numbers = list(numbers)

    for i in range(1, len(numbers) + 1):
        al = list(map(''.join, permutations(numbers, i)))
        al = list(set(al))
        al = list(map(int, al))
        print(al)
        for j in range(0, len(al)):
            pl.append(al[j])

    pl = list(set(pl))
    for i in range(0, len(pl)):
        if isPrimeNumber(pl[i]):
            answer += 1
    return answer

def isPrimeNumber(n):
    n = int(n)
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True