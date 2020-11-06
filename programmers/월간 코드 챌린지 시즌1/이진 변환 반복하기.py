def solution(s):
    cnt, zero_cnt = 0, 0
    while s != "1": # 1이 될 때까지 반복하기 위한 조건
        cnt += 1 # 이진 변환의 횟수 저장
        zero_cnt += s.count("0") # 변환 과정에서 제거되는 0의 개수 저장
        s_one = ''.join(s.split("0")) # 0 제거
        c = len(s_one) 
        s = str(bin(c)[2:]) # 길이를 2진법으로 표현한 문자열로 저장
    answer = [cnt, zero_cnt]
    return answer


s = "110010101001"
print(solution(s))