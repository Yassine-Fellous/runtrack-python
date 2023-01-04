def vi():
    i = 0
    while i <= 1000:
        j = 1
        k = 0
        while j <= i:
            if i % j == 0:
                k = k + 1
            j = j + 1
        if k == 2:
            print(i)
        i = i + 1

vi()
