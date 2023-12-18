#14889
#2022.07.27

import sys
from itertools import permutations

N=int(sys.stdin.readline())

S=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
print(S)
number=[i for i in range(N)]
print(number)

team1=[]
team2=[]
answer=[]
for team in permutations(number, N//2):
    team1.append(team)
print(team1)
