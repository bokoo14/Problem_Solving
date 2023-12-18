#10250
#2022.07.07
import sys

T=int(sys.stdin.readline())

for i in range(0, T):
    #층수, 방 수, 몇 번째 손님
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H ==0:
        floor=H
        room=(N // H)
    else:
        floor=N % H
        room =(N // H) +1
    print(floor*100+room)
    

