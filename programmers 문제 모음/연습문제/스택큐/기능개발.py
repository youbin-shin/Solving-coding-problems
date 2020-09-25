import math

def solution(progresses, speeds):
    period = [] # 작업이 완료되는 기간을 저장할 리스트
    N = len(progresses)
    for i in range(N):
        time = math.ceil((100 - progresses[i]) / speeds[i])
        period.append(time) # 작업이 완료될 기간을 계산하여 저장

    answer = []
    temp = period[0]
    cnt = 1
    for j in range(1, N):
        if temp >= period[j]: # 작업 시간이 temp보다 작은 경우
            cnt += 1 # 배포된 기능 개수 1 더하기
        else: # 이후 작업 시간이 temp보다 큰 경우
            answer.append(cnt)
            temp = period[j]
            cnt = 1 
    if temp:
        answer.append(cnt)
    return answer


# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# print(solution(progresses, speeds))