# 2023.02.04
import sys
input = sys.stdin.readline

n, s = map(int, input().split()) # 수열의 길이, 합 S이상이 되는 것 중 가장 짧은 것의 길이
a = list(map(int, input().split())) # 수열

left, right = 0, 0
answer=10**9
tmp=0
while True:
    if tmp>=s:
        answer=min(answer, right-left)
        tmp-=a[left]
        left+=1
    elif right==n:
        break
    else:
        tmp+=a[right]
        right+=1

if answer==10**9:
    print(0)
else:
    print(answer)