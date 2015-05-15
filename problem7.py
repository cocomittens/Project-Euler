def isPrime(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

def findNthPrime(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    count = 3
    num = 3
    while count <= n:
        num += 2
        if isPrime(num):
            count += 1
    return num

result = findNthPrime(10001)
print(result)
