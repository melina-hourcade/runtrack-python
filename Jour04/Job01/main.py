nombreEntier = int(input("Entrer un nombre"))

def Factorisation (a):
    if (a <= 1):
        return 1
    else:
        return Factorisation( a - 1 ) * a
    
print(Factorisation(nombreEntier))