num = 0
product = 0

for i in range(999):
  for j in range(999):
    product = i * j
    if str(product) == str(product)[::-1] and product > num:
        num = product

print(num)
