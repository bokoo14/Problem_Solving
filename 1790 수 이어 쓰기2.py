#1790 수 이어 쓰기2
#2022.08.13
#이분 탐색 알고리즘

import sys
input=sys.stdin.readline
#1~N까지의 수, 이어 쓴 수의 k번째 자리 수
N, k=map(int, input().split())

digit=1 #몇번째 자리수인지
nine=9
number=0 #몇개의 숫자가 있는지

while digit*nine<k:
    k-=(digit*nine)
    number=number+nine
    digit+=1
    nine=nine*10

answer=(number+1)+(k-1)//digit

if answer>N:
    print(-1)
else:
    print(str(answer)[(k-1)%digit])

    
'''
#메모리 초과
import sys
input=sys.stdin.readline

#1~N까지의 수, 이어 쓴 수의 k번째 자리 수
N, k=map(int, input().split())
n=[i for i in range(N+1)] #1~N까지의 수

number=''
for i in range(1, N+1):
    number+=str(n[i])

if len(number)<k:
    print(-1)
else:
    print(number[k-1])

'''


