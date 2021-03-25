def swim(n, price, d, m, m3):
    global minPrice
    if n > 12:
        if minPrice > price:
            minPrice = price
    elif price >= minPrice: # 이미 최소비용이 넘어갔기에 제외! (가지치기)
        return
    else:
        swim(n + 1, price + min(d*plan[n], m), d, m, m3) # n월 1일권과 1달권 비교
        swim(n + 3, price + m3, d, m, m3) # n월 3달 이용권


for t in range(1, int(input())+1):
    d, m, m3, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    minPrice = y
    swim(1, 0, d, m, m3)
    print('#{} {}'.format(t, minPrice))