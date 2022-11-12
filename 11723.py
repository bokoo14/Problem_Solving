#11723
#2022.06.30

#if문 많이 쓰면 시간 초과
#set을 쓰면 추가할때 그 값이 있으면 자동으로 중복 제거
#삭제할때 그 값이 없으면 자동으로 무시

import sys

N=int(sys.stdin.readline())

s=set()
for i in range(0, N):
    command=sys.stdin.readline().split()

    if len(command)==1:
        if command[0]=='all':
            s=set([x for x in range(1, 21)])
        elif command[0]=='empty':
            s=set()

    else:
        command[1]=int(command[1])
        if command[0]=='add':
            s.add(command[1])
        elif command[0]=='remove':
            s.discard(command[1])
        elif command[0]=='check':
            if command[1] in  s:
                print('1')
            else:
                print('0')
        elif command[0]=='toggle':
            if command[1] in s:
                s.discard(command[1])
            else:
                s.add(command[1])
