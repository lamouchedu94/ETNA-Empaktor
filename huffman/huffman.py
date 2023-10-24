import math
def occurence(chaine) :
    dico = {}
    for car in chaine :
        if car in dico :
            dico[car] += 1
        else : 
            dico[car] = 1
    return dico

chaine = "Le codage de Huffman est un algorithme de compression de données sans perte. Le codage de Huffman utilise un code à longueur variable pour représenter un symbole de la source (par exemple un caractère dans un fichier). Le code est déterminé à partir d'une estimation des probabilités d'apparition des symboles de source, un code court étant associé aux symboles de source les plus fréquents. "
dico = occurence(chaine)

def tri(dico) :
    res = []
    while len(dico) > 0 :
        max = -math.inf
        car_min = ""
        for occu in dico :
            if dico[occu] > max :
                max = dico[occu]
                car_min = occu
        res.append((car_min, dico[car_min]))
        del(dico[car_min])
    
    return res

