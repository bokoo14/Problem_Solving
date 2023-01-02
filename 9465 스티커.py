# 2023.01.02
import sys
input = sys.stdin.readline

t = int(input()) #test case
for i in range(t):
    col = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    for j in range(1, col):
        if j==1:
            sticker[0][1]+=sticker[1][0]
            sticker[1][1]+=sticker[0][0]
        else:
            sticker[0][j]+=max(sticker[1][j-1], sticker[1][j-2])
            sticker[1][j]+=max(sticker[0][j-1], sticker[0][j-2])

    print((max(sticker[0][col-1], sticker[1][col-1])))
    sticker.clear()

