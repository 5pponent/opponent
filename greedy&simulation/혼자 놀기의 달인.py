# 1. 2~100 중 자연수 하나 select
# 2.  해당 수 이하의 카드들을 상자에 하나씩 넣음
# 3. 상자를 섞어 일렬로 나열
# 4. 나열되면 순서대로 1~ 숫자 부여
# 5. 임의의 상자 하나를 까서 카드 숫자 확인
# 6. 확인한 카드의 숫자를 가진 상자를 까서 또 카드 숫자 확인
# 7. 다음에 열 상자가 오픈되어 있을 때 까지 반복
# 8. 이렇게 연 상자들을 1번 그룹
# 9. 1번 그룹을 격리, 이 때 1번 그룹 외 안 깐 상자가 없다면 게임 끝, 점수 0
# 10. 5~7을 한 번 더 반복하여 2번 그룹으로 편성
# 11. 1번 그룹 상자 수와 2번 그룹 상자 수를 곱한 값이 점수
# 상자 안에 들어간 카드 번호가 순서대로 담긴 배열을 cards로 드림
# 이 게임에서 얻을 수 있는 최대 점수 반환하셈
# cards len: 2~100, cards는 길이 이하의 자연수를 원소로 가짐, 중복 x, cards[i]는 i + 1번 상자에 담긴 카드 숫자를 말함

def solution(cards):
    li = []

    for i in range(len(cards)):
        li.append(search(cards, i))

    sorted(li, reverse=True)
    return li

def search(cards, start):
    visited = []
    visited.append(cards[start])
    target = cards[start] - 1

    while True:
        if cards[target] in visited: break
        visited.append(cards[target])
        target = cards[target] - 1

    return len(visited)

solution([8,6,3,7,2,5,1,4])