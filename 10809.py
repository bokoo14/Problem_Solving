#10809
#2022.07.31

import sys

array=list(sys.stdin.readline().strip())
alpha=[0]*(len(array))
for i in range(len(array)):
    alpha[i]=ord(array[i])-97

for i in range(26):
    if i in alpha:
        print(alpha.index(i), end=" ")
    else:
        print(-1, end=" ")

        

