for tc in range(int(input())):
    N, M = map(int, input().split())
    cnt = 0
    adj = {i: [] for i in range(1, N + 1)}
    for i in range(M):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    friends = [] # 상원이가 초대할 친구들 리스트
    invited = [0] * (N+1) # 초대를 받았는 지 확인하기 위한 리스트
    for j in range(len(adj[1])):
        invited[adj[1][j]] = 1
        friends.append(adj[1][j]) # 상원이가 초대한 친구들을 friends 리스트에 넣어준다.
        cnt += 1 # 상원이가 초대할 친구 수 카운트

    while friends: # 상원이의 친구의 친구들이 초대할 친구들
        f = friends.pop() 
        for k in range(len(adj[f])):
            if invited[adj[f][k]] == 0: # 상원이는 모르고 상원이 친구의 친구일 경우
                invited[adj[f][k]] = 1
                cnt += 1
    if invited[1]: cnt -= 1 # 상원이 혼자(1번학생이 상원이니까)일 경우 cnt에서 1을 빼준다.
    print('#{} {}'.format(tc+1, cnt))