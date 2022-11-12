#11659
#2022.07.09
'''
일일이 부분합을 구해주면 시간 초과!
미리 합을 다 계산해줬다가 나중에 필요한 값을 출력
'''
import sys

#수의 개수, 합을 구해야 하는 횟수
N, M = map(int, sys.stdin.readline().split())
array=list(map(int, sys.stdin.readline().split()))
asum=[0]

ss=0
for i in array:
    ss+=i
    asum.append(ss)

for i in range(M):
    a, b=map(int, sys.stdin.readline().split())
    print(asum[b]-asum[a-1])
    
