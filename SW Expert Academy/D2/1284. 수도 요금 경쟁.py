T = int(input())

for tc in range(T):
    P, Q, R, S, W = map(int, input().split())
    A_price = W * P
    if W <= R:

        B_price = Q
    else:
        B_price = Q + (W - R) * S

    final_price = min(A_price, B_price)

    print('#{} {}'.format(tc+1, final_price))