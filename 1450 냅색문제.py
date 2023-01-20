# 2023.01.19
import sys
input = sys.stdin.readline

n, c = map(int, input().split()) # 물건, 최대 무게
item = list(map(int, input().split()))

item1 = item[:n//2]
item2 = item[n//2:]
sum1=[]
sum2=[]

def bruteforce(item, sum, index, weight):
    if index>=len(item):
        sum.append(weight)
        return
    bruteforce(item, sum, index+1, weight) # 선택 X
    bruteforce(item, sum, index+1, weight+item[index]) # 선택 O

# item배열, 찾고자하는 값, 처음 index, 마지막 index
def binarysearch(item, target, start, end):
    while start<end:
        mid = (start+end)//2
        if item[mid]<=target:
            start=mid+1
        else: # item[mid]>target일때 -> 내가 원하는 값이 현재 check하는 값보다 작을때
            end=mid
    # binaysearch후의 index값이 내가 구하는 값의 개수를 나타냄
    return end

bruteforce(item1, sum1, 0, 0)
bruteforce(item2, sum2, 0, 0)
sum2.sort() # 이진탐색을 위해 정렬

answer=0
for s in sum1:
    if c<s: # 최대값보다 sum1의 값이 더 크면 answer에 더해주지 않음
        continue
    # return값: 더하는 값이 내가 원하는 값 이하인 경우의 수
    answer+=binarysearch(sum2, c-s, 0, len(sum2))
print(answer)
