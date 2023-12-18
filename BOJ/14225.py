#14225
#2022.07.28
'''
#브루트포스, 백트래킹

#브루트포스, 조합을 이용
import sys
from itertools import combinations

S = int(sys.stdin.readline())
num=list(map(int, sys.stdin.readline().split()))


sumnum=[False]*((sum(num)+2))

for i in range(1, S+1):
    com=list(combinations(num, i))
    ss=0
    for c in com:
        ss=sum(c)
        sumnum[ss]=True

for i in range(1, len(sumnum)+1):
    if sumnum[i]==False:
        print(i)
        break

'''
#브루트포스, 재귀
import sys
from itertools import combinations

S=int(sys.stdin.readline())
num=list(map(int, sys.stdin.readline().split()))

sumnum=[False]*((sum(num)+2))

def subset(index, s):
    
    if index>=S:
        return

    s+=num[index]
    sumnum[s]=True
    
    subset(index+1, s-num[index]) #선택 X
    subset(index+1, s) #선택 O


subset(0, 0)
for i in range(1, len(sumnum)+1):
    if sumnum[i]==False:
        print(i)
        break
    
    
    

    
    
