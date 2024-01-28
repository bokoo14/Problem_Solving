def fib(n):
    f=[0, 1] +[0]*(n-1)
    for i in range(2, n+1):
        f[i]=f[i-1]+f[i-2]
    return f

fiboArray=fib(50000) # 피보나치 수 50000개 만들기