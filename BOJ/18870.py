#18870
#2022.07.23

'''
set으로 중복 제거
dic의 시간복잡도: O(1)
'''

import sys

N=int(sys.stdin.readline())
array=list(map(int, sys.stdin.readline().split()))


array2=sorted(list(set(array)))
dic={array2[i]: i for i in range(len(array2))}

for i in array:
    print(dic[i], end=' ')

    
