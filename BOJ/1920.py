#1920
#2022.06.26

n = int(input())
#시간을 줄이기 위해 set으로 받아야 함
#list로 받으면 시간 초과
A=set(map(int, input().split())) 


m = int(input())
B = list(map(int, input().split()))

for i in range(0, m):
    if B[i] in A:
        print("1")
    else:
        print("0")
