#1541
#2022.07.10
'''
수학, 문자열, 파싱, 그리디 알고리즘
'''

import sys

line=sys.stdin.readline().strip().split('-')

for i in range(len(line)):
    s=line[i].split('+')
    ss=0
    for k in range(len(s)):
        ss+=int(s[k])
    line[i]=ss


for i in range(1,len(line)):
    line[0]-=line[i]

print(line[0])
