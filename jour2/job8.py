def saison(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")

    elif type == "fruits" and saison == "ete":
        print("pore, fraise et cassis")

    elif type == "legumes" and saison == "hiver":
        print("carrote, topinombour, endive et kiwi")

    elif type == "legumes" and saison == "ete":
        print("artichaut, aubergine, navet")

saison("legumes", "hiver")