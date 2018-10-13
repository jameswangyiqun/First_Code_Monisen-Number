def primeNumber(n):
    global result
    if n <= 1:
        result = False
    elif n == 2 or n == 3:
        result = True
    elif n % 2 == 0:
        result = False
    else:
        result = True
        for i in range(3, n, 2):
            if n % i == 0:
                result = False
                break
    return result

x = 1
for p in range(2,100):
    if primeNumber(p):
        m = 2 ** p - 1
        if primeNumber(m):
            print(x, p, m)
            x += 1
            if x > 7:
                break


