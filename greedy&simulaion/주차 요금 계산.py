import math

tmp = {}
result = {}
answer = []


def solution(fees, records):
    for data in records:
        result[parse(data)[1]] = 0

    for data in records:
        time, carNum = parse(data)
        if carNum in tmp:
            result[carNum] += time - tmp.pop(carNum)
        else:
            tmp[carNum] = time

    for carNum, time in tmp.items():
        result[carNum] += 1439 - time

    for carNum, time in result.items():
        result[carNum] = calFee(time, fees)

    for i in sorted(result.items()):
        answer.append(i[1])
    return answer


def parse(string):
    data = string.split(" ")
    time = data[0].split(":")
    return int(time[0]) * 60 + int(time[1]), data[1]


def calFee(time, fees):
    basic, basicFee, each, eachFee = fees
    if (time < basic):
        return basicFee
    else:
        return basicFee + math.ceil((time - basic) / each) * eachFee
