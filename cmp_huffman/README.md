# Algorithme de compression d'Huffman

## Introduction
La compression d'Huffman consiste en la création d'un arbre binaire composé de noeuds. Cet arbre permet de donner un codage pour chaque caractères. Pour la décompression la table de hachage est requise.

### Algorithme 
L'algoritme de compression d'Huffman et le suivant :
- On cherche l'occurence des caractères dans la chaine.
- On construit l'arbre. Les caractères les plus fréquents sont les plus haut dans l'arbre et inversement.
- On construit la table de hachage en parcourant l'arbre

### Prototype
```
Idk for the moment
```

### Paramètre
- data : La chaîne de caractères à transformer.


### Retourne
- La chaine codée
- La table de hachage

## Description 
L'agorithme de compression de **Huffman** fonctionne en créant un arbre binaire contenant les caractères de la chaine. Les caractères les plus fréquents sont les plus haut dans l'arbre et inversement. Nous devons créer une table de hachage pour pouvoir décoder la chaine par la suite. Pour créer cette table il suffit de parcourir l'arbre et de trouver le codage de chaque caractères.

Il est possible de retrouver la chaine original en appliquant la table de hachage à la chaine codée. 

