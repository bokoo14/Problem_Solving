#2798
#2022.07.07

'''
브루트포스 알고리즘
'''

import sys

N, M = map(int, sys.stdin.readline().split())

card=list(map(int, sys.stdin.readline().split()))

sum=0
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i]+card[j]+card[k] > M:
                continue
            else:
                sum=max(sum, card[i]+card[j]+card[k])

print(sum)
