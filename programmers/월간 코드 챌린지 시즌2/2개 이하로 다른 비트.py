# Solution 1

from collections import deque

def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = deque(int(i) for i in bin(number)[2:])
        # 비트 변환했을 때 0이 존재하는 경우
        if bin_number.count(0): 
            length = len(bin_number)
            for i in range(length - 1, -1, -1):
                if bin_number[i] == 0: # 가장 끝 쪽에 0을 1로 바꾸기
                    bin_number[i] = 1
                    if i != length - 1: 
                        # 가장 작은 수가 되기 위해서 1로 바꾼 뒤의 수 0으로 변경
                        bin_number[i + 1] = 0
                    break
        # 비트 변환했을 때 0이 존재하지 않는 경우
        else:
            bin_number.insert(1, 0) # 가장 작은 수이기 위한 조건 (ex. 11 -> 101)
        next_number = "0b" + "".join(map(str, bin_number))
        next_number = int(next_number, 2)
        answer.append(next_number)
    return answer


# Solution 2 (시간 초과 발생, 완전 탐색 방법)
def solution(numbers):
    answer = []
    def change_num_to_bits(num):
        bits = ""
        while True:
            q, r = divmod(num, 2)
            bits += str(r)
            if q == 1:
                bits += "1"
                break
            else:
                num = q
        return bits

    def check_bits_diff(bit1, bit2):
        max_length = max(len(bit1), len(bit2))
        if max_length > len(bit1):
            bit1 += "0" * (max_length - len(bit1))
        elif max_length > len(bit2):
            bit2 += "0" * (max_length - len(bit2))

        diff_cnt = 0
        for i in range(max_length):
            if bit1[i] != bit2[i]:
                diff_cnt += 1
        return diff_cnt

    for number in numbers:
        num_bit = change_num_to_bits(number)
        temp_num = number + 1
        while True:
            temp_bit = change_num_to_bits(temp_num)
            diff_cnt = check_bits_diff(num_bit, temp_bit)
            if diff_cnt <= 2:
                answer.append(temp_num)
                break
            temp_num += 1
    return answer