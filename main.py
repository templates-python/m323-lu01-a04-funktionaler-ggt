def ggt(a, b):
    if b == 0:
        return a
    else:
        return ggt(b, a % b)



if __name__ == '__main__':
    zahl1 = 56
    zahl2 = 48
    resultat = ggt(zahl1, zahl2)
    print(f"Der GGT von {zahl1} und {zahl2} ist {resultat}")  # Ausgabe: Der GGT von 56 und 48 ist 8