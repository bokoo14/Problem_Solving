#1463
#2022.06.30

#dp로 풀어야 함!
'''
동적계획법은 메모이제이션 방법을 사용해 중복되어 계산되는 값을 저장해 효율을 높여줌
연산의 홧수를 d[]에 저장하여 가장 작은 값을 출력해준다
'''

import sys

x=int(sys.stdin.readline())

d=[0]*(x+1)
for i in range(2, x+1):
    d[i]=d[i-1]+1
    if i % 3==0:
        d[i]=min(d[i], d[i//3]+1)
    if i % 2==0:
        d[i]=min(d[i], d[i//2]+1)

print(d[x])


'''
#단순 조건문으로 하면 반례가 생김
count=0
while x>0:
    if x%3==0:
        x=x//3
        count+=1
    elif x%2==0:
        x=x//2
        count+=1
    else:
        x-=1
        count+=1

print(count)
'''
