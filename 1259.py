#1259
#2022.07.01

#리스트에 넣어서 리스트를 뒤집어서 비교
import sys

while True:
    n=sys.stdin.readline().strip()
    if n=='0':
        break

    n=str(n)
    a=list(n)
    b=list(n)
    a.reverse()
    if a==b:
        print('yes')

    else:
        print('no')

'''
#str을 뒤집어서 비교
import sys

while True:
    n=sys.stdin.readline().strip()
    if n=='0':
        break

    if n==n[::-1]:
        print('yes')

    else:
        print('no')

'''
