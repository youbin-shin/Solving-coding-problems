from itertools import permutations

def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1): # 모든 경우의 순열을 찾기 위한 조건
        for j in permutations(numbers, i):
            temp = int("".join(j)) # 순열의 한 경우를 정수로 저장
            frag = True # 소수인지 판단 기준이 되는 변수
            if temp in [0, 1] or temp in answer: continue # 소수가 아닌 경우
            for k in range(2, temp):
                if temp % k == 0: # 소수가 아닌 경우
                    frag = False
                    break
            if frag: # 소수인 경우
                answer.append(temp)
    return len(answer)


numbers = "17"
print(solution(numbers))