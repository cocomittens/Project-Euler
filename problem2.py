def fib_sum(n):
    a = 1
    b = 2
    sum = 2
    while b <= n:
        b = b + a
        a = b - a
        if b % 2 == 0:
            sum = sum + b
    print (sum)

fib_sum(4000000)
