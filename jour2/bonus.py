def triangle(ab, bc ,ac):
    if ab + bc > ac and ac + bc > ab and ab + ac > bc:
        print("il est possible de réaliser ce triangle")
    else :
        print('ce triangle est impossible a réaliser')
    if pow(bc,2) == pow(ac,2) + pow(ab,2) or pow(ac,2) == pow(ab,2) + pow(bc,2) or pow(ab,2) == pow(ac,2) + pow(bc,2):
        print('ce triangle est rectangle')
    elif ab == bc or bc == ac or ac == ab:
        print('ce triangle est isocèle')
    elif ab == bc and bc == ac:
        print('ce triangle est equilatéral')
    else:
        print ('ce triangle est quelquonque')

# Isocèle rectangle
triangle(6, 6, 8.485281374249)

# Isocèle
triangle(3.6, 3.6, 5)

# Quelquonque
triangle(3, 4, 5)

# Equilatéral
triangle(3, 3, 3)

# Rectangle
triangle(4.8, 5.2, 2)

#Triangle impossible
triangle(-3,-5,3)

