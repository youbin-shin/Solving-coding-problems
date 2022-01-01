def solution(lottos, win_nums):
    ranking = [6, 6, 5, 4, 3, 2, 1]
    zero_cnt = lottos.count(0)
    win_cnt = len([i for i in lottos if i in win_nums])
    answer = [ranking[win_cnt + zero_cnt], ranking[win_cnt]]
    return answer