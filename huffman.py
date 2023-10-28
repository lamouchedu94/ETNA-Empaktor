import argparse
import math

def occurence(chaine):
    dico = {}
    for car in chaine:
        if car in dico:
            dico[car] += 1
        else:
            dico[car] = 1
    return dico

def tri(dico):
    res = []
    while len(dico) > 0:
        max_occu = -math.inf
        car_min = ""
        for occu in dico:
            if dico[occu] > max_occu:
                max_occu = dico[occu]
                car_min = occu
        res.append((car_min, dico[car_min]))
        del dico[car_min]
    return res

def n(dico):
    tab_noeud = tri(dico)
    while len(tab_noeud) > 1:
        derniers = ((tab_noeud[-1], tab_noeud[-2]), tab_noeud[-1][1] + tab_noeud[-2][1])
        poid_derniers = derniers[1]
        tab_noeud = tab_noeud[0:len(tab_noeud) - 2]
        trouve = False
        for i in range(len(tab_noeud)):
            if poid_derniers > tab_noeud[i][1]:
                temp = tab_noeud[0:i]
                temp.append(derniers)
                temp += tab_noeud[i:len(tab_noeud)]
                tab_noeud = temp
                trouve = True
                break
        if not trouve:
            tab_noeud.append(derniers)
    return tab_noeud

def codage(noeud, res, chemin):
    if type(noeud[0]) == str:
        res[noeud[0]] = chemin
        return
    codage(noeud[0][0], res, chemin + "0")
    codage(noeud[0][1], res, chemin + "1")

def encode(tab, chaine):
    res = {}
    codage(tab[0], res, "")
    codee = ""
    for car in chaine:
        codee += res[car]
    return codee, res

def decode(codee, dico):
    enclair = ""
    while len(codee) > 0:
        for cles in dico:
            if codee.startswith(dico[cles]):
                enclair += cles
                codee = codee[len(dico[cles]):]
    return enclair

def initialize_dico(chaine):
    dico = {}
    for car in chaine:
        if car in dico:
            dico[car] += 1
        else:
            dico[car] = 1
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ .,()":
        if char not in dico:
            dico[char] = 0
    return dico

def compress_huffman(chaine):
    dico = initialize_dico(chaine)
    tab = n(dico)
    codee, dico = encode(tab, chaine)
    return codee, dico

def decompress_huffman(codee, dico):
    return decode(codee, dico)

data = "aabbbccdddd"
compressed_data = compress_huffman(data)
print("Données compressées:", compressed_data)