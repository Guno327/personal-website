import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def exp(x, y, n):
    if y == 0:
        return 1
    else:
        z = exp(x, (int)(y/2), n)
        if y % 2 == 0:
            return (z*z) % n
        else:
            return (x * (z*z)) % n


def ee(a, b):
    if b == 0:
        return [1, 0, a]
    else:
        result = ee(b, a % b)
        return [result[1], result[0] - (int)(a / b) * result[1], result[2]]


def inverse(a, n):
    result = ee(a, n)
    if result[2] == 1:
        return result[0] % n
    else:
        return "none"


def isprime(p):
    nums = [2, 3, 5]
    for a in nums:
        if exp(a, p-1, p) != 1:
            return "no"
    return "yes"


def key(p, q):
    n = p * q
    phi = (p-1) * (q-1)

    e = 2
    while gcd(e, phi) != 1:
        e = e + 1

    d = inverse(e, phi)

    return n, e, d


lines = sys.stdin.readlines()

for line in lines:
    line_parts = line.split(' ')
    if line_parts[0] == "gcd":
        print(gcd(int(line_parts[1]), int(line_parts[2])))
    elif line_parts[0] == "exp":
        print(exp(int(line_parts[1]), int(line_parts[2]), int(line_parts[3])))
    elif line_parts[0] == "inverse":
        print(inverse(int(line_parts[1]), int(line_parts[2])))
    elif line_parts[0] == "isprime":
        print(isprime(int(line_parts[1])))
    elif line_parts[0] == "key":
        n, e, d = key(int(line_parts[1]), int(line_parts[2]))
        print(n, e, d)

