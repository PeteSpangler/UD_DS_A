def fibbonaci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibbonaci(n - 1) + fibbonaci(n - 2)

for i in range(20):
    print(fibbonaci(i))