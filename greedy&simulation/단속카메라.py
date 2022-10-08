def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    answer = 0

    for start, end in routes:
        if start > camera:
            camera = end
            answer += 1

    return answer