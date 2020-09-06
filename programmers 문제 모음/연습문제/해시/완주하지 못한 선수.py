def solution(participant, completion):
    answer = ''
    # participant, completion 모두 정렬
    participant.sort()
    completion.sort()
    answer = participant[-1] # completion과 동일하면 마지막 값이 답이 되기에 미리 저장
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
    return answer


# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
# print(solution(participant, completion))