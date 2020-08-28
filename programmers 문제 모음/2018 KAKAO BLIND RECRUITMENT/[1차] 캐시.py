from collections import deque

def solution(cacheSize, cities):
    for c in range(len(cities)): # 대소문자 구분이 없기에 소문자로 통일하기
        cities[c] = cities[c].lower()
    answer = 0
    cache_list = deque()
    if cacheSize == 0: 
        answer = len(cities) * 5
    else:
        for i in range(len(cities)):
            # 도시이름이 캐시에 없을 경우
            if cities[i] not in cache_list: 
                if len(cache_list) == cacheSize:
                    cache_list.pop()
                cache_list.appendleft(cities[i])
                answer += 5
            
            # 도시이름이 캐시에 있을 경우
            else:
                cache_list.remove(cities[i])
                cache_list.appendleft(cities[i])
                answer += 1

    return answer

# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# print(solution(cacheSize, cities))