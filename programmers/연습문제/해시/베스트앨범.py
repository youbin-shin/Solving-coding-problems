def solution(genres, plays):
    answer = []
    genre_dict = {}
    # 속한 노래가 많이 재생된 장르 순서 찾기
    for g in range(len(genres)):
        if genres[g] in genre_dict:
            genre_dict[genres[g]] += plays[g]
        else:
            genre_dict[genres[g]] = plays[g]
    genre_dict = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)

    # 장르 내 많이 재생된 노래 수록하기
    for gd in genre_dict:
        temp = []  # 같은 장르 노래 저장할 리스트
        for i in range(len(genres)):
            if gd[0] == genres[i]:
                temp.append([i, plays[i]])
        # 장르 내에서 재생 횟수가 높을 수록, 같으면 고유 번호가 낮은 순으로 정렬하기
        temp = sorted(temp, key=lambda x: (-x[1], x[0]))
        for t in range(len(temp)):
            if t == 2:  # 두개씩 출시하기에 필요한 조건
                break
            answer.append(temp[t][0])
    return answer


# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
# print(solution(genres, plays))
