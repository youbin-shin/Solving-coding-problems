# sol1 : 16진수 직접 계산
for tc in range(int(input())):
    N, K = map(int, input().split())
    n = N//4
    nums = list(input())
    result = []
    for _ in range(n+1):
        for n1 in range(0, N, n):
            cal = 0
            cnt = 1
            for n2 in range(n1+n-1, n1-1, -1):
                if nums[n2] in 'ABCDEF': # A ~ F
                    cal += cnt * (ord(nums[n2]) - 55)
                else:
                    cal += cnt * int(nums[n2])
                cnt *= 16
                if n2 == n1 and cal not in result:
                    result.append(cal)
        nums.insert(0, nums.pop())

    result.sort(reverse=True)
    print('#{} {}'.format(tc+1, result[K-1]))


# sol2 : int 성질 이용
# int('16진수', 16) = 10진수로!!

for tc in range(int(input())):
    N, K = map(int, input().split())
    n = N//4
    nums = list(input())
    result = []
    for _ in range(n+1):
        for n1 in range(0, N, n):
            cal = ''
            for n2 in range(n1, n1+n):
                cal += nums[n2]
            cal = int(cal, 16)
            if cal not in result:
                result.append(cal)
        nums.insert(0, nums.pop())

    result.sort(reverse=True)
    print('#{} {}'.format(tc+1, result[K-1]))


# sol2-2 : int 성질 이용
for tc in range(int(input())):
    N, K = map(int, input().split())
    codes = list(map(str, input()))
    line = N//4
    numbers = []
    for i in range(line):
        for j in range(0, N, line):
            numlst = codes[j:j+line] # 한 변의 숫자들을 numlst에 저장하기
            num = int(''.join(numlst), 16) # 리스트를 16진수로 바꾸기
            if num not in numbers:
                numbers.append(num)
        codes.append(codes.pop(0))
    numbers.sort(reverse=True) # 내림차순으로 정리하기
    print('#{} {}'.format(tc+1, numbers[K-1]))