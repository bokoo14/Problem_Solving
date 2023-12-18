# 2023.02.05
import sys
input = sys.stdin.readline

n = int(input()) # 숫자 카드의 개수
nCard = sorted(list(map(int, input().split()))) # 숫자 카드
m = int(input()) # 확인할 숫자카드의 개수
mCard = list(map(int, input().split())) # 확인할 숫자 카드

answer = [] # 상근이가 가지고 있으면 1, 아니면 0
for findingCard in mCard:
    start, end = 0, n-1
    while start<=end:
        mid = (start+end)//2
        if nCard[mid]==findingCard:
            answer.append("1")
            break
        elif nCard[mid]>findingCard: # 찾는 값보다 현재 indexd의 값이 더 크면
            end = mid-1
        elif nCard[mid]<findingCard:
            start=mid+1
    else:
        answer.append("0")

print(*answer)