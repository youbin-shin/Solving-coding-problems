from itertools import combinations

N = int(input())
Slist = [list(map(int, input().split())) for _ in range(N)]
start_team_list = list(combinations(list(i for i in range(N)), int(N/2))) # 조합을 통해 반을 나눠준다.
final_value = 1000000000
for i in range(len(start_team_list)):
    start_team = []
    link_team = []
    start_force = 0
    link_force = 0
    for n in range(N):
        if n in start_team_list[i]:
            start_team.append(n)
        else:
            link_team.append(n)
    # 능력치를 더해주기 위해 팀내에서 2명씩 뽑는다.
    start_team_force = list(combinations(start_team, 2)) 
    link_team_force = list(combinations(link_team, 2))
    # 능력치를 더해준다.
    for stf in start_team_force:
        start_force += Slist[stf[0]][stf[1]] + Slist[stf[1]][stf[0]]
    for ltf in link_team_force:
        link_force += Slist[ltf[0]][ltf[1]] + Slist[ltf[1]][ltf[0]]
    # 능력치의 차이가 적은 값을 저장한다.
    if final_value > abs(start_force - link_force):
        final_value = abs(start_force - link_force)
print(final_value)