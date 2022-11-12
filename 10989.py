#10989
#2022.07.08

'''
for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리 비효율
메모리를 좀 더 효율적으로 관리해주어야 한다
sort를 쓰지 않고, 리스트에 각 요소마다 0을 할당해놓고
입력받을 때마다 그 입력값을 같은 인텍스에 +1씩 해준다
입력을 다 받고 나면 0보다 큰 요소를 갖는 인덱스들을 찾아서 그 수만큼 인텍스 출력
'''
import sys

n=int(sys.stdin.readline())

array=[0]*10001
for i in range(0, n):
    array[int(sys.stdin.readline())]+=1


for i in range(0, 10001):
    if array[i]!=0:
        for j in range(0, array[i]):
            print(i)

