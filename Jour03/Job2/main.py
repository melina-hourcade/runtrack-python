nombre = int(input("Entrez un nimbre entier "))

def puissance(x, nbdePuissance):
    if (nbdePuissance == 0):
        return 1
    else:
        return puissance(x, nbdePuissance - 1 ) * x

print(puissance(10,nombre))