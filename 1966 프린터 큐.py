import sys
input = sys.stdin.readline

t = int(input()) # test case
for i in range(t):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))
    index=0
    answer=0
    while 1:
        if max(number)==number[index]: # 가장 큰 값을 프린트해줌
            answer+=1
            if index==m:
                print(answer)
                break
            else:
                number[index]=-1
                index=(index+1)%n
        else:
            index=(index+1)%n
