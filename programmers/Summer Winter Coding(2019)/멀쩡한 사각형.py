def solution(w, h):
    if w < h :
        w, h = h, w
    def gcd(bigNum, smallNum): # 최대공약수 찾기
        global temp
        if bigNum % smallNum == 0:
            return smallNum
        else:
            return gcd(smallNum, bigNum % smallNum)
    temp = gcd(w, h)
    answer = w * h - (w + h - temp) # 모든 정사각형 개수 - 사용할 수 없는 정사각형 개수
    return answer


print(solution(8, 12))