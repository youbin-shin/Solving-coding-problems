tc = int(input())
for t in range(tc):
    N, K = map(int, input().split())
    K -= 1
    student_lst = [[0 for _ in range(3)] for _ in range(N)]
    score_lst = [0]*N
    clscore_lst = [0]*N

    grade = ['A+', 'A0', 'A-','B+', 'B0', 'B-','C+', 'C0', 'C-','D0']
    for i in range(N):
        student_lst[i] = list(map(int, input().split()))
        score_lst[i] = round(student_lst[i][0]* 0.35 + student_lst[i][1]* 0.45 + student_lst[i][2]* 0.20, 2)
    clscore_lst = list(score_lst)
    clscore_lst.sort(reverse=True)
    gradeidx = clscore_lst.index(score_lst[K])//(N//10)

    print('#{} {}'.format(t+1,grade[gradeidx]))