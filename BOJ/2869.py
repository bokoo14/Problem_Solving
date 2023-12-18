#2869
#2022.06.27
import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

#마지막 밤에 미끄러지는 것을 고려: V-B
day=(V-B)/(A-B)

print(math.ceil(day))



'''
#반복문으로 풀면 시간초과
while V>0:
    V=V-total
    if V!=0:
        count+=1

print(count)
'''

