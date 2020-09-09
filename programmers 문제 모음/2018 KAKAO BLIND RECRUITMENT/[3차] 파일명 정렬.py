def solution(files):
    answer = []
    files_list = []
    string_list = [" ", ".", "-"]
    for i in range(len(files)):
        temp = files[i]
        number = ""
        head = ""
        tail = ""
        for j in range(len(temp)):
            if temp[j].isalpha() or temp[j] in string_list or len(number) == 5:
                if number != "" : # tail 저장
                    tail = temp[j:]
                    break
                else: # head 저장
                    head += temp[j]
            else: # number 저장
                number += temp[j]
        files_list.append([head, number, tail])
    # head 기준, number 기준으로 정렬
    files_list = sorted(files_list, key = lambda x : (x[0].lower(), int(x[1])))
    for k in range(len(files_list)): # 정렬을 다시 문자열로 합쳐 answer에 저장
        temp = files_list[k][0] + str(files_list[k][1]) + files_list[k][2]
        answer.append(temp)
    return answer


# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# print(solution(files))
