def sumOfSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

def squareOfSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    sum = sum**2
    return sum

result = sumOfSquares(100) - squareOfSum(100)
print(result)
