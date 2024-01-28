'''
어떤 정수 X를 1로 만들고자 한다.
사용할 수 있는 연산은 다음과 같은 세 가지 연산이 있다.
1. X가 3의 배수이면 3으로 나누기
2. X가 2의 배수이면 2로 나누기
3. X에서 1을 빼기
양의 정수 N이 주어졌을 때, 위와 같은 세 가지 연산을 사용해서 1을 만들기 위해
사용해야 하는 연산의 최솟값을 출력하시오.
단, 위의 방법으로 1로 만들 수 없는 경우는 존재하지 않는다고 가정해도 된다.
'''

import sys
input=sys.stdin.readline

x=int(input()) 
d=[0]*(x+1) 
for i in range(2,x+1):
    d[i]=d[i-1]+1 
    if i%3==0: 
        d[i]=min(d[i],d[i//3]+1)
    if i%2==0: 
        d[i]=min(d[i],d[i//2]+1)
print(d[x])