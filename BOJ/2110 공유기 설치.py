#2110 공유기 설치
#2022.08.17
#이분탐색
'''
1. array라는 리스트에 집들의 좌표를 입력받은 후에 정렬.
2. start = 1, end = array[-1] - array[0] 으로 설정. (시작값은 최소 거리, 끝 값은 최대 거리 )
3. 앞 집부터 공유기 설치
4. 설치할 수 있는 공유기 개수가 c개를 넘어가면 더 넓게 설치할 수 있다는 이야기 이므로 설치거리를 mid + 1로 설정하여 다시 앞집부터 설치.
5. c개를 넘어가지 않는다면 더 좁게 설치해야 한다는 이야기 이므로 mid - 1로 설정.
'''
import sys
input=sys.stdin.readline
#집, 공유기
N, C = map(int, input().split())
home=[0]*(N)
for i in range(N):
    home[i]=int(input())

home.sort()

#거리의 최소값, 최대값
start=1 #거리 최소값
end=home[-1]-home[0] #거리 최대값

while start<=end:
    mid=(start+end)//2 #공유기 설치 거리
    current=home[0] #공유기를 처음 설치하는 곳
    install=1 #공유기 설치 수

    for i in range(1, len(home)):
        if home[i]>=current+mid:
            install+=1 #공유기 설치
            current=home[i] #다음 공유기를 설치할 위치


    #일단 공유기를 모두 설치하고 검사
    if install>=C: #install(설치한 공유기 수)가 많으면
        start=mid+1 #설치거리를 더 넓게 해준디
        answer=mid
    else: #설치거리를 더 좁게 해준다
        end=mid-1


print(answer)
            
