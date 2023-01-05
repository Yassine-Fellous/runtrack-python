L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
i = 0
a = L[0]
b = L[0]
while i < len(L):
    if L[i] < a:
        a = L[i]
    elif L[i] > b:
        b = L[i]
    i +=1

print(a)
print(b)