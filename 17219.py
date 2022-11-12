#17219
#2022.06.30

#리스트로 하면 시간 초과 O(n)
#딕셔너리로 하면 시간 O(1)

import sys

N, M = map(int, sys.stdin.readline().split())

site={}
password={}
for i in range(0, N):
    s, p= sys.stdin.readline().split()
    s=s.strip()
    p=p.strip()
    site[s]=p

for i in range(0, M):
    find=str(sys.stdin.readline().strip())
    print(site[find])
