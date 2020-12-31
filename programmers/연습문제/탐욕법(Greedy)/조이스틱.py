def solution(name):
    answer = 0
    cursorCheck = False
    cursorLocation = []
    # 조이스틱 위아래로 움직이는 횟수
    for n in range(len(name)):
        if name[n] == "A":
            cursorCheck = True
        else:
            cursorLocation.append(n)  # A가 아닌 인덱스 저장
        answer += min(abs(ord("A") - ord(name[n])), abs(ord("Z") - ord(name[n]) + 1))

    # 조이스틱 좌우로 움직이는 횟수
    if cursorCheck:  # "A"가 있는 경우 최소 조작 횟수 계산
        idx = 0
        cnt = 0
        if idx in cursorLocation:  # 0 인덱스는 이동할 필요 없기에 제거
            cursorLocation.remove(idx)
        while cursorLocation:
            minDiff = float("inf")  # 가장 최소 이동 거리
            changeIndex = -1  # 이동해야할 인덱스
            for c in cursorLocation:
                # 오른쪽으로 가는 것이 최소일지 왼쪽으로 가는 것이 최소일지 가장 최솟값 diff 에 기록
                diff = min(abs(idx - c), abs(len(name) - c + idx))
                if minDiff > diff:
                    minDiff = diff
                    changeIndex = c
                    print(cursorLocation, changeIndex, minDiff)
            if changeIndex != -1:
                cnt += minDiff
                idx = changeIndex
                cursorLocation.remove(idx)
        answer += cnt
    else:  # "A"가 없는 경우 조작 횟수 계산
        answer += len(name) - 1
    return answer


## 예시 test case
# name = "JEROEN"
# name = "JAN"
## 테스트 케이스 11 이 틀릴 경우 반례
# name = "BBBAAAB"
# name = "ABABAAAAABA"

# print(solution(name))
