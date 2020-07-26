def cal(idx, result, oper1, oper2, oper3, oper4):
    global final_max, final_min
    if idx == N: # 끝까지 계산이 됐을 경우 비교한 뒤 종료해준다.
        if final_max < result:
            final_max = result
        if final_min > result:
            final_min = result
        return
    if oper1:
        cal(idx+1, result + Alst[idx], oper1-1, oper2, oper3, oper4)
    if oper2:
        cal(idx+1, result - Alst[idx], oper1, oper2-1, oper3, oper4)
    if oper3:
        cal(idx+1, result * Alst[idx], oper1, oper2, oper3-1, oper4)
    if oper4:
        if result > 0:
            cal(idx+1, int(result/Alst[idx]), oper1, oper2, oper3, oper4-1)
        else:
            cal(idx+1, int(-(abs(result)/Alst[idx])), oper1, oper2, oper3, oper4-1)


N = int(input())
Alst = list(map(int, input().split()))
oper1, oper2, oper3, oper4 = map(int, input().split()) # +, -, *, / 의 개수를 의미한다.
final_max = -999999999
final_min = 999999999
cal(1, Alst[0], oper1, oper2, oper3, oper4)
print(final_max)
print(final_min)