def from_ten_to_base(n, base):
    n = int(n)
    res = ''
    while n != 0:
        if n % base > 9:
            res += 'ABCDEF'[n % base - 10]
        else:
            res += str(n % base)
        n //= base
    return res[::-1]

def from_base_to_ten(n, base):
    n = str(n)
    res = 0
    for i in range(len(n)):
        if n[::-1][i] in 'ABCDEF':
            res += ('ABCDEF'.index(n[::-1][i]) + 10) * base ** i
        else:
            res += int(n[::-1][i]) * base ** i
    return str(res)

def transformation(n):
    n9 = from_ten_to_base(n, 9)

    for i in range(5):
        if n9.count('5') == n9.count('7'):
            n9 += n9[-1]
        else:
            A = []
            for i in n9:
                if n9.count(i) == n9.count(max(n9, key=lambda x: n9.count(x))) and int(i) not in A:
                    A.append(i)
            n9 += str(max(A))
    return from_ten_to_base(from_base_to_ten(n9, 9), 16)

for i in range(10000, 10, -1):
    if 'BAC' in transformation(i):
        print(i)
        break











