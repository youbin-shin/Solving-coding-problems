def backtrack(k, hsum):
    global result
    if hsum >= shelf: # 가지치기 (없어도 동작함 => 없애면 메모리는 적게 사용하나 실행시간은 더 빨라진다.)
        if hsum - shelf < result: # 선반과 키 합의 차이가 최소 차이값보다 작으면 변경
            result = hsum - shelf
            return
    if k == people: 
        if hsum >= shelf and hsum - shelf < result:
            result = hsum - shelf
    else:  # 조합 이용
        backtrack(k + 1, hsum + heights[k]) # k번째 점원 포함
        backtrack(k + 1, hsum) # k 번째 점원 포함 x


for tc in range(int(input())):
    people, shelf = map(int, input().split())
    heights = list(map(int, input().split()))
    result = 99999999999999
    if shelf >= sum(heights): # 키를 다 합쳐도 선반보다 작은 경우 바로 계산하기
        result = shelf - sum(heights)
    else:
        backtrack(0, 0)
    print('#{} {}'.format(tc+1, result))