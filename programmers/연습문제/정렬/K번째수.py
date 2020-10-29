def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        i, j, k = commands[c][0]-1, commands[c][1], commands[c][2]
        temp = array[i:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer


# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array, commands))