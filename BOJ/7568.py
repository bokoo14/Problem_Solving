#7568
#2022.06.27
import sys

n=int(sys.stdin.readline())

person =[]
for i in range(0, n):
    person.append()

#행 기준 정렬
person.sort(key=lambda x:x[0])

#열 기준 정렬
person.sort(key=lambda x:x[1])


for i in range(0, n):
    print(person[i][0], person[i][1])

