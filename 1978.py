#1978
#2022.06.26

n = int(input())
A = list(map(int, input().split()))
cnt=0

for i in A:
    for j in range(2, i+1):
        if i%j == 0:
            if i == j:
                cnt+=1

            break
        
            
#소수의 갯수 출력
print(cnt)
