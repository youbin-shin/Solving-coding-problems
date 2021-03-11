def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        check = -1
        flag = True # 가능한 스킬트리인지 알려주는 변수
        for st in skill_tree:
            if st in skill:
                if check + 1 == skill.index(st): # 순서대로 배우는지 체크하는 조건
                    check = skill.index(st)
                else:
                    flag = False
                    break
        if flag:
            answer += 1

    return answer


# skill = "CBD"
# skill_trees = ["CED"]
# print(solution(skill, skill_trees))