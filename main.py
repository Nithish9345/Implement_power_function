def power(a, x, m):
    if x == 0:
        return 0
    if x == 1:
        return a
    p = power(a, x//2, m)

    if x % 2 == 0:
        return (p*p) % m
    else:
        return (p * p *a) % m

print(power(a= int(input()), x= int(input()), m=int(input())))


