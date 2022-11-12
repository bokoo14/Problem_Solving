#13549 숨바꼭질3
#2022.08.05
#너비우선탐색, 0-1너비우선탐색
import sys
input=sys.stdin.readline
from collections import deque

#수빈, 동생
N, K = map(int, input().split())
dp=[0]*(100001)

def bfs(x):
    queue=deque()
    queue.append(x)

    while queue:
        a=queue.popleft()
        if a==K:
            print(dp[K])
            return
        for i in (2*a, a-1, a+1): #2*a먼저 해줘야됨. 우선순위 고려
            if 0<=i<=100000 and dp[i]==0:
                if i==2*a:
                    dp[i]=dp[a]
                    queue.append(i)
                elif i==a-1 or i==a+1:
                    dp[i]=dp[a]+1
                    queue.append(i)

bfs(N)
        


