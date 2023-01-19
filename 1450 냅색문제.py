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
    bruteforce(item, sum, index+1, weight)
    bruteforce(item, sum, index+1, weight+item[index])

def binarysearch(item, target, start, end):
    while start<end:
        mid = (start+end)//2
        if item[mid]<=target:
            start=mid+1
        else:
            end=mid
    return end

bruteforce(item1, sum1, 0, 0)
bruteforce(item2, sum2, 0, 0)
sum2.sort()

answer=0
for s in sum1:
    if c<s:
        continue
    answer+=binarysearch(sum2, c-s, 0, len(sum2))
print(answer)
