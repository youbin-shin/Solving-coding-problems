from datetime import datetime
from math import ceil


def solution(fees, records):
    # 자동차별 주차 시간 정보 정리
    cars = dict()
    for record in records:
        times, num, types = map(str, record.split(" "))
        num = int(num)
        if num not in cars:
            cars[num] = times
        else:
            cars[num] += "," + times
    # 자동차별 주차 요금 계산
    for car, value in cars.items():
        time_list = list(map(str, value.split(",")))
        if len(time_list) % 2 == 1:
            time_list.append("23:59")
        time_diff = 0
        for i in range(0, len(time_list), 2):
            start = datetime.strptime(time_list[i], "%H:%M")
            end = datetime.strptime(time_list[i + 1], "%H:%M")
            time_diff += (end - start).seconds // 60

        default_time, default_fee, unit_time, unit_fee = fees
        if time_diff <= default_time:
            cost = default_fee
        else:
            cost = default_fee + ceil((time_diff - default_time) / unit_time) * unit_fee
        cars[car] = cost
        
    return [cost for num, cost in sorted(cars.items())]