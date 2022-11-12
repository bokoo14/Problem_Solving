#10816
#2022.06.29

import sys
from collections import Counter

N=int(sys.stdin.readline())
have=list(map(int, sys.stdin.readline().split()))


M=int(sys.stdin.readline())
exam=list(map(int, sys.stdin.readline().split()))


#리스트에서 개수를 세주고 그 값이 몇개있는지 세주고 딕셔너리에 저장
count = Counter(have)

total=len(exam)
for i in range(0, total-1):
    if exam[i] in count:
        print(count[exam[i]], end=" ")
    else:
        print(0, end=" ")


if exam[total-1] in count:
    print(count[exam[total-1]], end="")
else:
    print(0, end="")

