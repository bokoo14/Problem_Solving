from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        answer = 5*len(cities)
    else:
        for city in cities:
            city = city.lower() # 대소문자 구분X
            if city in cache: # cache hit
                answer+=1
                cache.remove(city)
                cache.append(city)
            else: # cache miss
                answer+=5
                if len(cache) >= cacheSize:
                    cache.popleft()
                    cache.append(city)
                else:
                    cache.append(city)
                    
    return answer