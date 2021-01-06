
p = 499
q = 269
n = p * q
f = (p - 1) * (q - 1)

def euclid(a, b):
    while b:
        c = a % b
        a = b
        b = c

    return a

e = 2
while (e < f):
    if euclid(e, f) == 1:
        break
    else:
        e = e + 1

d = 1
while True:
    r = (d * e) % f
    if r == 1: break
    d = d + 1

def criptare(text, n, e):
    text_crypto = ""
    criptate = []
    for litera in text:
        l = ord(litera)
        c = (l**e) % n
        criptate.append(c)

    for i in criptate:
        text_crypto += str(i) + " "

    return text_crypto

def decriptare(text, n, d):
    text_clar = ""
    number = 0
    list = []
    for t in text:
        if t.isdigit():
            number = number * 10 + int(t)
        else:
            list.append(number)
            number = 0

    list.append(number)

    for c in list:
        m = (c**d) % n
        litera = chr(m)
        text_clar += litera

    return text_clar
