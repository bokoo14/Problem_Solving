#2675
#2022.08.02

import sys
input=sys.stdin.readline

P=int(input())

for i in range(P):
    cycle, string = map(str, input().split())
    cycle=int(cycle)
    answer=''
    for j in range(len(string)):
        answer=answer+string[j]*cycle

    print(answer)
