#BOJ 1546

print("과목수를 입력하세요!")
num = int(input())
#배열 리스트로 선언
array = []
calcgrage = []

aver = 0

for i in range (0, num):
    array = input()


def math(array):
    maxgrade = max(array)
    for i in range(0, num):
        calcgrade[i] = array[i]/maxgrade*100
        

def average():
    for i in range (0, num):
        aver = aver + array[i]
    aver = aver/num


math(array)
average()
print(aver)
