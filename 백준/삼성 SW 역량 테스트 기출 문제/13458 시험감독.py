N = int(input())
candidate = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = N # 각 시험장에 총감독관은 오직 1명 있어야 하는 조건
for i in range(len(candidate)):
  people = candidate[i]
  if people - B > 0: # 감시가 필요한 사람들이 있으면 부감독관 추가
    diff = people - B
    q, r = divmod(diff, C)
    cnt += q
    if r != 0: cnt += 1

print(cnt)