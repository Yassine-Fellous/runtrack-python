def l():
    L=[1, 2, 3, 4, 5]
    L[3] = L[2] + L[4]
    return(L)

print(l()[1])
print(l()[4])
print(l()[3])

