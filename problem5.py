def divisible(n):
    lowestMultiple = n
    isLowestMultiple = False
    while True:
        for i in range(1, n+1):
            if lowestMultiple % i != 0:
                isLowestMultiple = False
                lowestMultiple += n
                break
            else:
                isLowestMultiple = True
        if isLowestMultiple:
            return lowestMultiple

result = divisible(20)
print(result)
