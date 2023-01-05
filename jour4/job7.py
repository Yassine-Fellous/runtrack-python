
L = [8, 24, 48, 2, 16]
n = 0
a = 0
while n < len(L):
    if L[n] % 3 == 0:
        a = a + 1
    n = n + 1

print(a)
