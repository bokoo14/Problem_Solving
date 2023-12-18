#2022.06.26(일)
#1181

#단어의 개수와 단어들을 입력받아 정렬
n=int(input())
word_list = []
for i in range(0, n):
    word_list.append(input()) #배열의 끝에 해당하는 단어를 추가


#사전 정렬 후 단어의 길이가 짧은 순으로 정렬(선택 정렬 오름차순)
#중복 제거
word_set=set(word_list)
word_list = list(word_set)

#사전 순 정렬
word_list.sort()
#길이 순 정렬
word_list.sort(key=len)

for i in word_list:
    print(i)
    





	
