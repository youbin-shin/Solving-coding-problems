def solution(phone_book):
    answer = True
    frag = 1
    for i in range(len(phone_book)):
        if frag == 2: break
        for j in range(i+1, len(phone_book)):
            a = phone_book[i]
            b = phone_book[j]
            if len(a) > len(b): a, b = b, a
            if a == b[:len(a)]: # 접두어가 같은 경우 false
                answer = False
                frag = 2
                break
    return answer


# phone_book = ["119", "97674223", "1195524421"]
# print(solution(phone_book))