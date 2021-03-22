# sol 1
for t in range(int(input())):
    card = input()
    cardlist = [0]*(len(card)//3)
    for i in range(len(card)//3):
        cardlist[i] = card[3*i:3*i+3]
    cardnums = [13, 13, 13, 13]
    ans = ''

    if len(set(cardlist)) != len(cardlist):
        ans = 'ERROR'

    else:
        for i in range(len(cardlist)):
            if cardlist[i][0] == 'S':
                cardnums[0] -= 1
            elif cardlist[i][0] == 'D':
                cardnums[1] -= 1
            elif cardlist[i][0] == 'H':
                cardnums[2] -= 1
            else:
                cardnums[3] -= 1

        for i in range(4):
            ans += str(cardnums[i]) + ' '

    print('#{} {}'.format(t+1, ans))



# # sol 2
# for tc in range(1, int(input()) + 1):
#     arr = input()
#     # 필요한 카드 개수
#     cnt = [13] * 4

#     # 개별 카드 정보를 식별, 3개씩 읽어오기
#     cards = set()
#     for i in range(0, len(arr), 3):  # 카드 시작 위치
#         temp = arr[i: i + 3]  # 카드 중복 체크를 위해
#         if temp in cards:
#             cnt = 'ERROR'
#             break  # ERROR
#         cards.add(temp)
#         if temp[0] == 'S':
#             cnt[0] -= 1
#         elif temp[0] == 'D':
#             cnt[1] -= 1
#         elif temp[0] == 'H':
#             cnt[2] -= 1
#         else:
#             cnt[3] -= 1
#     print(cnt)