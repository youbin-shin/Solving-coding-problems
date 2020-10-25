def solution(skill, skill_trees):
    skill = list(skill)
    skill_trees = [list(st) for st in skill_trees]
    answer = 0
    for i in range(len(skill_trees)):
        before = -1
        frag = True # 가능한 스킬트리인지 알려주는 변수
        for j in range(len(skill)):
            if skill[j] in skill_trees[i]:
                temp = skill_trees[i].index(skill[j])
                if before == -1 and j != 0: # 첫번째 스킬을 배우지 않고 다음 스킬을 먼저 배우는 경우
                    frag = False
                    break
                elif before < temp:
                    if j != 0 and skill_trees[i][before] != skill[j-1]: # 이전 스킬을 배우지 않고 다음 스킬을 배우는 경우
                        frag = False
                        break
                    else:
                        before = temp
                else: # 스킬의 인덱스(temp)가 이전의 인덱스(before)보다 큰 경우
                    frag = False
                    break
        if frag:
            answer += 1
    return answer


# skill = "CBD"
# skill_trees = ["CED"]
# print(solution(skill, skill_trees))