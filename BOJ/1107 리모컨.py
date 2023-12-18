#2023.01.08
import sys
input=sys.stdin.readline

n = int(input()) #이동하려는 채널
m = int(input()) #고장난 버튼의 개수
button= list(map(int, input().split())) #고장난 버튼

answer = abs(100-n) # 최소 몇번 누를지
for i in range(1000001):
    press=1
    i = str(i)
    # 현재 채널의 각 자리수를 check -> 고장난 버튼이 있다면 버튼을 누르지 못함
    for j in range(len(i)):
        if int(i[j]) in button:
            press=0
            
    # 현재 채널의 버튼을 누를 수 있다면
    if press:
        answer = min(answer, abs(int(i)-n)+len(i))

print(answer)