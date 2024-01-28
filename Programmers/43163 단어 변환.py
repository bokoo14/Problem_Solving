from collections import deque

# 단어 비교 & 1개만 차이날때 check
def checkWords(target, trans):
    diffCount = 0
    for i in range(len(target)):
        if list(target).pop(i) != list(trans).pop(i):
            diffCount += 1
            
    return diffCount == 1

def solution(begin, target, words):
    if target not in words: # 내가 찾는 단어가 배열 내에 없다면 변환할 수 없음
        return 0
    
    isTrans = False
    visited = [0] * len(words) # 단어를 변환한 적 있는지 check
    q = deque()
    q.append([begin, 0])
    answer = 0

    while q:
        w, wCount = q.popleft() # 현재의 단어
        if w == target:
            isTrans = True
            answer = wCount
        for i in range(len(words)):
             # 아직 변환한 적이 없고, 단어를 변환할 수 있다면
            if visited[i] == 0 and checkWords(w, words[i]):
                q.append([words[i], wCount+1])
                visited[i] = 1 # 방문

    return answer if isTrans else 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))