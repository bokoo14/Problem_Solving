from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list) # 기본 형식이 리스트인 딕셔너리 생성

    for start, end in tickets:
        graph[start].append(end)
    
    '''
    알파벳 역순으로 정렬하는 이유는, 
    각 도착지를 알파벳이 큰 순서대로 고려하여 경로를 구성하면, 
    알파벳이 작은 도착지는 나중에 사용될 가능성이 높아지기 때문입니다.
    이는 다음과 같은 이유로 알파벳 역순으로 정렬하는 것이 유리합니다. 
    '''
    for key in graph.keys(): # 그래프의 value값들을 알파벳 역순으로 정렬 (알파벳 역순으로 pop하여 경로를 구성하기 위함)
        graph[key].sort(reverse=True)

    def dfs(start, route): # 시작 노드, 경로를 담은 배열
        nonlocal answer
        # 도착 여부 체크
        if len(route) == len(tickets) + 1: # 모든 경로를 다 탐색했다면
            if not answer or route < answer:
                answer = route
            return

        for i, destination in enumerate(graph[start]): # enumerate: index와 값을 동시에 반환, 해당 노드와 연관된 모든 값 탐색
            if destination != "used": # 사용하지 않았다면
                graph[start][i] = "used" # 방문했음을 표시하고 재귀
                dfs(destination, route + [destination]) # 재귀로 구현
                graph[start][i] = destination # 재귀 호출이 끝나면, 해당 도착지를 다시 사용 가능한 상태로 되돌립니다.

    dfs("ICN", ["ICN"])
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))