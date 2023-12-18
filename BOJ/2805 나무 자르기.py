#2023.01.06
import sys
input=sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
while start<=end:
    answer=0
    cut = (start+end)//2
    for i in tree:
        if i>=cut: # 자르고 남은 나무 길이 더해줌
            answer+=(i-cut)
        
    if answer>=m: # 원하는 값보다 크거나 같으면 자를 나무 크기를 늘려봄
        start=cut+1
    else: 
        end=cut-1

print(end)