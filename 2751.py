#2751
#2022.06.27
import sys

n=int(input())
array=[]

for i in range(0, n):
    array.append(int(sys.stdin.readline()))

array.sort()

for i in range(0, n):
    print(array[i])
    


'''
#input으로 받으면 시간 초과
for i in range(0, n):
    array.append(int(input()))

#삽입 정렬
for i in range(0, n):
    compare=array[i]
    for j in range(i, n):
        if compare>array[j]:
            array[i], array[j] = array[j],array[i]


for i in range(0, n):
    print(array[i])
'''


