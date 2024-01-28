import sys
input = sys.stdin.readline

# 압축을 할 수 있는지 체크(모두 같은 값인지 체크)
# 흰색이면 0, 검정색이면 1
def check(i, j, n, A):
    chk = A[i][j]
    for r in range(i, i + n):
        for c in range(j, j + n):
            if A[r][c] != chk:
                return 2
    return chk


def quadtree(i, j, n, A):
    if n == 1: # 더이상 나눌 수 없으면
        return str(A[i][j])
    else:
        chk = check(i, j, n, A)
        if chk < 2: #같으면 (0 또는 1)
            return str(chk) 
        else: # 다르면 4개로 쪼개준다
            m = n//2
            s1 = quadtree(i, j, m, A)
            s2 = quadtree(i,j+m , m, A)
            s3 = quadtree(i+m, j , m, A)
            s4 = quadtree( i+m, j+m , m, A)
            return "(" + s1 + s2 + s3 + s4


N=int(sys.stdin.readline())
A=[list(map(int, input().split())) for _ in range(N)]
answer = list(quadtree(0, 0, N, A))

for i in range(len(answer)):
    if answer[i]=='1':
        answer[i]='B'
    elif answer[i]=='0':
        answer[i] = 'W'
    elif answer[i]=='(':
        answer[i] = 'Q'

print(N)
for i in range(len(answer)):
    print(answer[i], end = "")

