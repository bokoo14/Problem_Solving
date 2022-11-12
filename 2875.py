#2875 대회 or 인턴
#2022.08.09
#그리디 알고리즘
import sys
input=sys.stdin.readline

#여학생, 남학생, 인턴쉽 참여 인원
N, M, K = map(int, input().split())

team = min(N//2, M)

while ((N-2*team)+(M-team))<K:
    team-=1

print(team)
