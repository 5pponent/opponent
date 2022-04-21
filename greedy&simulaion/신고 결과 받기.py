def solution(id_list, report, k):
    answer = []
    report = set(report)
    stopped = set()
    dic = {id: [set(), 0] for id in id_list}

    while report:
        item = report.pop()
        신고자, 신고당한자 = item.split(" ")
        dic[신고자][0].add(신고당한자)
        dic[신고당한자][1] += 1
        if dic[신고당한자][1] == k:
            stopped.add(신고당한자)

    for id in dic.keys():
        answer.append(len(dic[id][0] & stopped))

    return answer