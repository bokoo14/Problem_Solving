# 2023.01.16
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 전위순회
preorder=[]
while True:
    try:
        preorder.append(int(input()))
    except:
        break

# 후위순회
def postorder(start, end):
    if start>end:
        return
    mid = end+1
    for i in range(start+1, end+1):
        if preorder[start]<preorder[i]:
            mid=i
            break
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(preorder[start])

postorder(0, len(preorder)-1)