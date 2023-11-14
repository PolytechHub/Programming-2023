def validate(n):
    s = 0
    for i in range(2, abs(n)):
        if n % i == 0:
            s += i
    return s == n

for i in range(1000000):
    if validate(i):
        print(i)