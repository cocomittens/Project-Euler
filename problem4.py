def palindrome(numDigits):
    num = 0
    product = 0

    for i in range(10**(numDigits)-1):
      for j in range(10**(numDigits)-1):
        product = i * j
        if str(product) == str(product)[::-1] and product > num:
            num = product

    return num

result = palindrome(3)
print(result)
