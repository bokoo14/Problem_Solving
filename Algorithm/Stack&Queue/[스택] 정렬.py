'''
강의교재에서 본 주차장의 주차 관리인에게 주차 주문이 도착했다.
이 주차 주문에 따르면, 1번부터 N번까지의 차량이 오른편에서 차례대로 도착하고 있을 때,
왼편의 주차 공간에 주차 주문의 차량 번호 순서에 따라 주차를 해야 한다.
이 주차장은 스택처럼 생긴 하단부의 임시 공간을 이용해서 주차 순서를 조정할 수밖에 없음을 알고 있을 것이다.
또한, 한 번 주차장 안으로 들어온 차량은 거꾸로 빼낼 수도 없다.
그렇기 때문에, 때로는 주차 주문에 적힌 주차 순서가 주차하기가 불가능한 순서일 수도 있다.
예를 들어, 주차 계획의 차량 번호 순서가 다음과 같다고 하자.
5 4 1 2 3
차량의 도착 순서가 1 2 3 4 5 이므로 5번 차량을 제일 안쪽으로 주차하려면 스택에 1 2 3 4를 차례대로 push해야 한다.
따라서, 5번 다음에 4번을 주차할 수는 있지만, 4번 다음에 와야 할 1번 차량은 스택의 아래쪽에 있으므로 4번 뒤에 주차할 수 없다.
M개의 주차 주문이 주어졌을 때, 이 주차 주문이 가능하면 "yes"를 불가능하면 "no"를 출력하시오
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
carorder = [list(map(int, input().split())) for _ in range(m)]

def sol(carorder):
    stack = []
    mycar = [i+1 for i in range(n)]
    parking=[]
    index=0
    while len(mycar):
        current = mycar.pop(0)
        stack.append(current)
        while len(stack) and stack[-1]==carorder[index]:
            parking.append(stack.pop())
            index+=1
    while len(stack):
        parking.append(stack.pop())
    return parking

def answer(a, b):
    if a==b:
        return 'yes'
    else:
        return 'no'

for i in range(m):
    print(answer(sol(carorder[i]), carorder[i]))

    