#1107
#2022.08.02
#브루트포스 알고리즘
import sys
input=sys.stdin.readline

N = int(input()) #이동하려는 채널
M = int(input()) #고장난 버튼의 개수
button= list(map(int, input().split())) #고장난 버튼

remote=[0,1,2,3,4,5,6,7,8,9,'+','-']

remote=list(set(remote)-set(button))


