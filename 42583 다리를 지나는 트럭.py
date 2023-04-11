from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0 #시간을 저장하기 위해
    bridge = deque([0]*bridge_length) #다리 위의 트럭들을 넣어서 나타내기 위해 bridge_length만큼 곱한 이유는 최대 bridge_length만큼 트럭이 다리에 올라갈수 있기 때문 예시를 보면 10이하를 만족해도 1초 텀을 두고 출발 but 100일 경우 낭비같기도해서 고민, but while문 반복할때 기본적으로 bridge_length만큼 반복해야 time +1 하기 좋음
    truck_weights = deque(truck_weights) #트럭들 각각의 무게가 담긴 배열을 데큐로 변환해서 사용할려고함
    total_bridge = 0 #sum을 이용하면 시간초과, 시간을 줄이기 위해
    while bridge: #브릿지가 텅 빌때까지
        time += 1 #1초 더함
        #bridge.popleft() #브릿지의 가장 앞을 빼냄
        total_bridge -= bridge.popleft() #브릿지의 가장 앞을 빼내면서 total_bridge를 조정한다
        if truck_weights: #만약 truck_weights에 원소가 있으면
            if total_bridge + truck_weights[0] <= weight: #현재 bridge에 있는 트럭들의 합 + 다음에 들어올 트럭들의 무게가 최대 무게 이하인지 검사, 최대무게 이하면 bridge에 추가
                tmp = truck_weights.popleft()
                bridge.append(tmp)
                total_bridge += tmp
            else: #0을 삽입하는건 시간을 위해
                bridge.append(0)
    return time