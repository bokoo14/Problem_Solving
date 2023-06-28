# 2023.06.20

import sys
input = sys.stdin.readline

n = int(input())
alpha = [input().strip() for _ in range(n)]

alpha = list(set(alpha))
alpha.sort(key = lambda x: (len(x), x))

for i in range(len(alpha)):
    print(alpha[i])
