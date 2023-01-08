#def rectangle(num1, num2):
#    i = "|" + "-" * num2 + "|" + " " * num2 + "\n|" * (num1 - 1) + "-" * num2 + "|"
#    print(i)
#
#rectangle(3,3)

def rectangle(num2, num1):
    i = "|" + "-" * num2 + "|" + " " * num2 + "\n"
    j = "|" + " " * num2 + "|" + " " * num2 + "\n"
    print(i + j * (num1 - 2) + i)

rectangle(10,3)



