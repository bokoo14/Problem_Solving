# 2023.02.10
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
def isContain(find, length, A):
    for i in range(length):
        if find==A[i]:
            return True
for _ in range(t):
    a = input().rstrip() # 암호화된 비밀번호
    b = input().rstrip() # 원래의 비밀번호
    balpha = [0 for _ in range(26)]
    for i in range(len(b)):# 원래의 비밀번호 알파벳 check
        balpha[ord(b[i])-97]+=1

    answer = False
    aalpha = [0 for _ in range(26)]
    for i in range(len(b)):
        aalpha[ord(a[i])-97]+=1
    for i in range(len(b), len(a)):
        if aalpha == balpha:
            answer = True
            break
        else:
            aalpha[ord(a[i-len(b)])-97]-=1 # 슬라이딩 윈도우의 제일 앞의 값을 뺴줌
            aalpha[ord(a[i])-97]+=1 # 슬라이딩 윈도우 오른쪽으로 한칸 이동
    if aalpha == balpha:
        answer = True
    print("YES" if answer==True else "NO")