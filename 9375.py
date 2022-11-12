#9375
#2022.07.01

'''
딕셔너리를 활용
하나의 key값에 여러개의 value값을 리스트 형태로 넣어준다
하나의 key값에 있는 value의 개수를 구하여 경우의 수를 구해줌

경우의 수: ((value의 수+1)*...*(value의 수+1))-1
하나도 안입은 경우 하나는 빼줌
'''

import sys

a=int(sys.stdin.readline())

for i in range(0, a):
    b=int(sys.stdin.readline())
    wear={}
    for j in range(0, b):
        value, key=map(str, sys.stdin.readline().split())

        if key not in wear.keys():
            wear[key]=[value]
        else:
            wear[key].append(value)
    answer=1
    for key in wear.keys():
        answer*=(len(wear[key])+1)
    print(answer-1)
