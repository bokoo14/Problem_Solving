#15829
#2022.07.09

'''
ord()함수를 사용해 아스키코드로 변환 (알파벳->숫자)
char()함수를 사용해 아스키코드로 변환 (숫자->알파벳)

A~Z: 65~90
a~z: 97~122
'''

import sys

n=int(sys.stdin.readline())
c=sys.stdin.readline()

answer=0
for i in range(n):
    answer+=(ord(c[i])-96)*(31**(i))
    
print(answer%1234567891)
