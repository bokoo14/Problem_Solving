#16198
#2022.07.29

'''
브루트포스, 백트레킹
'''
import sys

N=int(sys.stdin.readline())
W=list(map(int, sys.stdin. readline().split()))

answer=[]
def energy(total):
    if len(W)==2:
        answer.append(total)
        return
    
    for i in range(1, len(W)-1):
        e=W[i-1]*W[i+1]

        temp=W[i]
        del W[i]
        energy(total+e)
        
        W.insert(i, temp)

energy(0)
print(max(answer))

