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

criptate = []

def criptare(text, n, e):
    text_criptat = ""
    for litera in text:
        l = ord(litera)
        c = (l**e) % n
        criptate.append(c)
        a = (c % 26) + 65
        text_criptat += chr(a)

    return text_criptat

def decriptare(criptate, n, d):
    text_clar = ""
    for c in criptate:
        m = (c**d) % n
        litera = chr(m)
        text_clar += litera

    return text_clar

public_key = {"n": n, "e": e}
private_key = {"n": n, "d": d}
print(f"Public key: { public_key }")
print(f"Private key: { private_key }")

text_clar = input("Text: ")
text_clar = text_clar.upper()

text_criptat = criptare(text_clar, n, e)
print(text_criptat)
text_decriptat = decriptare(criptate, n, d)
print(text_decriptat)