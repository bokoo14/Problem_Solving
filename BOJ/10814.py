#10814
#2022.06.28

import sys

N=int(sys.stdin.readline())

person = []
for i in range(0, N):
    person.append(list(sys.stdin.readline().split()))

#나이 순 정렬(x[0]을 기준)
#x[0]은 
person.sort(key=lambda x:int(x[0]))

for i in range(0, N):
    print(person[i][0], person[i][1])
    

