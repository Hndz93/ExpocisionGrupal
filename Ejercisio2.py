def c(n):
    if n <2:
        return n
    return c(n-1) + c (n-1)
for x in range (20):
    print(c(x))