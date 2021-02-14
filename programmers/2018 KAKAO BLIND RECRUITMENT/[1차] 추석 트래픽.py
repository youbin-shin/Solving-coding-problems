def check(t, time_list): # t를 기준으로 1초 동안 처리량이 몇개인지 체크하는 함수
    cnt = 0
    start = t
    end = t + 1000 # 1초 뒤의 시간 저장하기
    for time in time_list:
        if time[1] >= start and time[0] < end: # 주어진 시간 간격이 [start, end] 안에 포함되는 경우
            cnt += 1 # 처리량 + 1
    return cnt


def solution(lines):
    answer = 1
    time_list = []
    for line in lines:
        date, time, duration = line.split()
        h, m, s = map(float, time.split(":")) # 시간, 분, 초로 나눠서 변수에 저장하기
        duration = float(duration.replace("s", "")) * 1000 # 문자 s 없애고 ms 단위로 바꾸기
        end = (h * 60 * 60 + m * 60 + s)* 1000 # 끝난 시간을 ms 단위로 바꾸기
        start = end - duration + 1 # 시작 시간 ms 단위로 구하기
        time_list.append([start, end])
    for t in time_list:
        answer = max(answer, check(t[0], time_list), check(t[1], time_list))
    return answer


# lines = [
#     "2016-09-15 20:59:57.421 0.351s",
#     "2016-09-15 20:59:58.233 1.181s",
#     "2016-09-15 20:59:58.299 0.8s",
#     "2016-09-15 20:59:58.688 1.041s",
#     "2016-09-15 20:59:59.591 1.412s",
#     "2016-09-15 21:00:00.464 1.466s",
#     "2016-09-15 21:00:00.741 1.581s",
#     "2016-09-15 21:00:00.748 2.31s",
#     "2016-09-15 21:00:00.966 0.381s",
#     "2016-09-15 21:00:02.066 2.62s"
# ]
# print(solution(lines))
