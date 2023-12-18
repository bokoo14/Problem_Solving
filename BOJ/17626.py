#17626
#2022.07.09

import sys

n=int(sys.stdin.readline())
dp=[0]*(n+1)
dp[0]=0
dp[1]=1

for i in range(2, n+1):
    minvalue=1e9
    j=1
    while(j**2)<=i:
        minvalue=min(minvalue, dp[i-(j**2)])
        j+=1
    dp[i]=minvalue+1

print(dp[n])
