#2108
#2022.06.30

import sys
from collections import Counter

N=int(sys.stdin.readline())

number=[]
for i in range(0, N):
    number.append(int(sys.stdin.readline()))

number.sort()

#평균
print(round(sum(number)/N))
#중앙값
print(number[N//2])
#최빈값
c=Counter(number).most_common(2)
if len(number)>1:
    if c[0][1]==c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])
#범위
print(max(number)-min(number))
