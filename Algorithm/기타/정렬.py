import sys
input = sys.stdin.readline
n=int(input())

array = [list(map(int, input().split())) for _ in range(n)]
# x좌표 증가하는 순, y좌표 감소하는 순, z좌표 증가하는 순
array.sort(key = lambda x : (x[0], -x[1], x[2]))


#문자열을 기준으로 정렬, 같은 문자일때 소문자가 먼저 나와야 한다
# A: 65 a: 97
# 대소문자 구분없이 정렬하고, 아스키코드 값을 이용해서 정렬
c = [list(map(int, input().split())) for _ in range(n)]
c.sort(key = lambda x : (x.upper(), -ord(x)))