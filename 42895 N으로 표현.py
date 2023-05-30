def solution(N, number):
    dp = [set() for i in range(9)]  # 사용횟수에 따라 가능한 숫자를 담을 리스트,set으로 중복제거
    for i in range(1, 9):  # 1~8
        dp[i].add(int(str(N) * i))  # 단순히 이어붙인 숫자 5면 55같은것들 i에 따라 555, 5555
        for j in range(i):
            for first in dp[j]:
                for second in dp[i - j]:
                    dp[i].add(first + second)
                    dp[i].add(first - second)
                    dp[i].add(second - first)
                    dp[i].add(first * second)
                    if second != 0:
                        dp[i].add(first // second)
                    if first != 0:
                        dp[i].add(second // first)
        if number in dp[i]:
            return i
    return -1
