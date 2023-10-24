def occurence(chaine) :
    dico = {}
    for car in chaine :
        if car in dico :
            dico[car] += 1
        else : 
            dico[car] = 1
    return dico
