# 2023.01.13
'''
import sys
input = sys.stdin.readline

y1, m1, d1 = map(int,input().split())
y2, m2, d2 = map(int,input().split())

# 윤년은 2월에 추가됨
def leapYear(year):
    if (year%4==0 and year%100!=0) or year%400==0: # 4로 나누어떨어지면 윤년
        return True
    else:
        return False

answer=0
days1=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days2=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y2-y1>1000: # 1000년이상이라면 gg를 출력
    print("gg")
elif y2-y1==1000:
    if m2-m1>0 or ((m2-m1)==0 and (d2-d1)>0):
        print("gg")
else:
    for i in range(y1+1, y2): # (y1+1) ~ (y2-1)까지 윤년인지 검사
        if leapYear(i): # 윤년이라면
            answer+=366
        else:
            answer+=365
    # 첫 해
    if leapYear(y1): # 윤년
        answer+=(sum(days2[m1+1:]))
        answer+=(days2[m1]-d1)
    elif not leapYear(y1): # 윤년이 아니면
        answer+=(sum(days1[m1+1:]))
        answer+=(days1[m1]-d1)
    # 마지막 해
    if leapYear(y2): # 윤년
        answer+=(sum(days2[:m2]))
        answer+=(d2)
    elif not leapYear(y2): # 윤년이 아니면
        answer+=(sum(days1[:m2]))
        answer+=(d2)
    
print("D-{}".format(answer))
        
'''

# D-Day
import datetime
import sys

Year1, Month1, Day1 = map(int, sys.stdin.readline().split(" "))
Year2, Month2, Day2 = map(int, sys.stdin.readline().split(" "))

start = datetime.date(Year1, Month1, Day1)
finish = datetime.date(Year2, Month2, Day2)

dDay = str(finish - start).split(" ")[0]
if int(dDay) >= 365243:
    print("gg")
else:
    print(f"D-{dDay}")
