def l():
    a = ["a", "b"]
    c = a[0]
    a[0] = a[1]
    a[1] = c
    return a

print(l())