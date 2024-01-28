import sys
import math
input = sys.stdin.readline

def is_prime(k):
    if k<2:
        return False
    else:
        for c in range(2, int(k**(0.5))+1):
            if k%c==0: # 나누어지는 값이 있으면 약수가 있음 = 소수가 아님
                return False
    return True


# 에라토스테네스체를 이용한 소수찾기
def solve(M, N):
    global sieve
    sieve = [1]*(N+1) #리스트에 값을 저장
    sieve[0]=sieve[1]= 0 #0과 1은 소수가 아니다
    for i in range(2, int(math.sqrt(N))+1):
        if sieve[i] >= 0: #sieve의 값이 
            for j in range(i*i, N+1, i): # i의 배수들
                sieve[j]=0 #배수들을 -0로 바꿔줌(소수가 아님)