#1157
#2022.08.02

import sys
input=sys.stdin.readline

word=input().strip().upper()
word_list=list(set(word))

cnt=[]
for i in word_list:
    cnt.append(word.count(i)) #요소가 몇 개 있는지 세준다


#최댓값의 개수가 많으면
if cnt.count(max(cnt))>1:
    print("?")
#최댓값이 한 개
else:
    i=cnt.index(max(cnt))
    print(word_list[i])
