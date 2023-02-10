# This is a sample Python script.
# le programme est fait en python.

# KAKA NZUKI MEDI L2 GENIE-INFO.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def OuExclusif(identifian_1, identifiant_2):
    res = ""
    tabeau = ["" for i in range(len(identifian_1))]
    for i in range(len(identifian_1)):
        variable_1 = identifian_1[i:i + 1]
        variable_2 = identifiant_2[i:i + 1]

        tabeau[i] = "0" if variable_1 == variable_2 else "1"

    for i in tabeau:
        res += i
    return res


def OuLogique(identifian_1, identifiant_2):
    res = ""
    tabeau = ["" for i in range(len(identifian_1))]
    for i in range(len(identifian_1)):
        variable_1 = identifian_1[i:i + 1]
        variable_2 = identifiant_2[i:i + 1]

        tabeau[i] = "1" if variable_1 == "1" or variable_2 == "1" else "0"

    for i in tabeau:
        res += i
    return res


def ETlogique(va11, identifiant_2):
    res = ""
    tabeau = [""] * len(va11)
    for i in range(len(va11)):
        variable_1 = va11[i:i + 1]
        variable_2 = identifiant_2[i:i + 1]
        tabeau[i] = "1" if variable_1 == "1" and variable_2 == "1" else "0"
    res = "".join(tabeau)
    return res



def permut(val, k):
    res = ""
    tabeau = [0] * len(val)

    for i in range(len(val)):
        id = k[i:i + 1]
        vid = int(id)
        tabeau[i] = val[vid]
        res += tabeau[i]
    #print("res permut", res)
    return res


def inverse_permut(k):
    res = ""
    tabeau = [0] * len(k)

    for i in range(len(k)):
        id = k[i:i + 1]
        vid = int(id)
        tabeau[vid] = str(i)

    res = ''.join(tabeau)
    #print("res inverse", res)
    return res


def decalage(val, ordre, gauche):
    res = ""
    tabeau = [""] * len(val)
    s = -1 if gauche else 1
    for i in range(len(val)):
        variable_1 = val[i:i + 1]
        o = ordre
        j = i
        while o > 0:
            if j + s < 0:
                j = len(val) - 1
            elif j + s >= len(val):
                j = 0
            else:
                j = j + s
            o -= 1
        tabeau[j] = variable_1
    res = "".join(tabeau)
    return res



def generateKey(k, pk, gdecalage, ddecalage):
    res = ""
    nk = permut(k, pk)
    k1 = nk[0:4]
    k2 = nk[4:8]
    nk1 = OuExclusif(k1, k2)
    nk2 = ETlogique(k1, k2)
    dnk1 = decalage(nk1, gdecalage, True)
    dnk2 = decalage(nk2, ddecalage, False)
    res = dnk1 + "," + dnk2
    #print("res keygen " + res)
    return res

def roundDChiffre(val, kp, k):
    res = ""
    perm = permut(val, kp)
    res = OuExclusif(perm, k)
    return res


def roundGChiffre(vald, valg, k):
    res = ""
    fc = OuLogique(valg, k)
    res = OuExclusif(vald, fc)
    return res

def roundGDechiffre(val, kp, k):
    res = ""
    nkp = inverse_permut(kp)
    c = OuExclusif(val, k)
    res = permut(c, nkp)
    return res


def roundDDechiffre(vald, valg, k):
    res = ""
    fc = OuLogique(valg, k)
    res = OuExclusif(vald, fc)
    return res



def main():
    print("********ALGORITHME DE FREISNEL CIPHER*********")
    print("Donnez une clé K de longueur 8")
    key = input()
    while len(key) < 8:
        print("La taille de la clé doit être de longueur 8")
        key = input()
    print("Donnez la fonction H de permutation")
    h = input()
    while len(h) < 8:
        print("La taille doit être de longueur 8")
        h = input()
    decg = 0
    decd = 0
    print("Entrez l'ordre de décalage à gauche")
    decg = int(input())
    while decg <= 0:
        print("L'ordre doit être supérieur à 0")
        decg = int(input())
    print("Entrez l'ordre de décalage à droite")
    decd = int(input())
    while decd <= 0:
        print("L'ordre doit être supérieur à 0")
        decd = int(input())
    kgen = generateKey(key, h, decg, decd)
    print("Entrez la valeur N ou C à traiter")
    n = input()
    while len(n) < 8:
        print("La taille doit être de longueur 8")
        n = input()
    choix = -1
    while choix != 1 and choix != 2:
        print("Voulez-vous chiffrer ou dechiffrer? (1 pour dechiffrer et 2 pour chiffrer)")
        choix = int(input())
    print("Entrez la permutation P de 4 bits")
    p = input()
    while len(p) < 4:
        print("La taille doit être de longueur 4")
        p = input()
    print("Entrez la clé de permutation pour l'opération de chiffrement ou déchiffrement")
    keyc = input()
    while len(keyc) < 8:
        print("La taille doit être de longueur 8")
        keyc = input()
    tkey = kgen.split(",")
    if choix == 2:
        pn = permut(n, keyc)
        g0 = pn[:4]
        d0 = pn[4:8]
        d1 = roundDChiffre(g0, p, tkey[0])
        g1 = roundGChiffre(d0, g0, tkey[0])
        d2 = roundDChiffre(g1, p, tkey[1])
        g2 = roundGChiffre(d1, g1, tkey[1])
        c = g2 + d2
        ikey = inverse_permut(keyc)
        res = permut(c, ikey)
        print("La valeur chiffrée est :", res)
    else:
        pn = permut(n, keyc)
        g2 = pn[:4]
        d2 = pn[4:8]
        g1 = roundGDechiffre(d2, p, tkey[1])
        d1 = roundDDechiffre(g2, g1, tkey[1])
        g0 = roundGDechiffre(d1, p, tkey[0])
        d0 = roundDDechiffre(g1, g0, tkey[0])
        Nd = g0 + d0
        ikey = inverse_permut(keyc)
        res = permut(Nd, ikey)
        print("La valeur déchiffrée est :", res)
main()
#test value to enter k 01101101 h 65274130 n 01101110 hh 46027315 P 2013 C : 10110010

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

