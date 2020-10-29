def solution(n, t, m, p): # n : 진법, t : 구해야할 갯수, m : 총 인원, p : 내순서
    answer = ''
    num = 1
    numbers = '0'
    numAlpha = ["A", "B", "C", "D", "E", "F", "G"] # 10 ~ 15 일 경우 대문자 출력하기 위한 리스트
    while len(numbers) < t * m:
        temp = num
        change_temp = "" # 수를 진법으로 바꿔 저장할 변수 (거꾸로 저장됨)
        while temp != 0:
            r = temp % n
            if r >= 10:
                change_temp += numAlpha[r - 10]
            else:
                change_temp += str(r)
            temp = int(temp // n)
        numbers += change_temp[::-1] 
        num += 1
    while len(answer) != t: # 자신이 말해야하는 수 저장하기
        answer += numbers[p - 1]
        p += m
    return answer


# n, t, m, p = 2, 4, 2, 1
# print(solution(n, t, m, p))