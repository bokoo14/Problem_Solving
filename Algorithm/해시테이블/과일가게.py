'''
N개의 과일 판매 목록이 주어졌을 때, 가장 많이 팔린 과일을 출력하시오.
만일, 가장 많이 팔린 과일이 여러 개 있으면, 알파벳 순서가 가장 빠른 과일을 출력하시오.

첫째 줄에 과일 판매 목록에서 가장 많이 팔린 과일의 이름을 출력한다.
만일, 가장 많이 팔린 과일이 여러 개 있으면, 알파벳 순서가 가장 빠른 과일을 출력한다.
둘째 줄에 가장 많이 팔린 과일이 몇 번 팔렸는지 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
fruit = [input().strip() for _ in range(n)]

sale = {}
def sol(fruit, n):
    for i in fruit:
        if i in sale:
            sale[i]+=1
        else:
            sale[i]=1

sol(fruit, n)
answer = sorted(sale.items(), key = lambda x: (-x[1], [x[0]]))
print(answer[0][0])
print(answer[0][1])

