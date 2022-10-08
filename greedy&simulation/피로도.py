import itertools

def solution(k, dungeons):
    total = 0

    for data in list(itertools.permutations(dungeons, len(dungeons))):
        tmp = k
        count = 0

        for item in data:
            if (tmp >= item[0]):
                tmp -= item[1]
                count += 1
            total = max(total, count)

    return total