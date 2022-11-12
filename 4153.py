#4153
#2022.06.30

#세값 중에 가장 큰 값을 구해서 미리 빼줘야 한다

import sys

while True:
    c=list(map(int, sys.stdin.readline().split()))

    if sum(c)==0:
        break

    max_a=max(c)
    c.remove(max_a)
    if (c[0]**2)+(c[1]**2)==(max_a**2):
        print('right')
    else:
        print('wrong')
