# Empaktor - Compression et décompression de fichiers

## Introduction

Empaktor est un outil de compression et de décompression de fichiers. Il prend en charge trois algorithmes de compression :

* **Huffman** : un algorithme de compression sans perte qui utilise une table de hachage pour encoder les données.
* **RLE** : un algorithme de compression sans perte qui utilise la répétition de séquences de caractères pour réduire la taille des données.
* **BWT** : un algorithme de compression sans perte qui utilise la transformée de Burrows-Wheeler pour réorganiser les données.

### Utilisation

Empaktor est utilisé via la ligne de commande. Pour compresser un fichier, utilisez la commande suivante :

`python3 empaktor.py <fichier.tar.gz> [--compression <algorithme>] --compress <fichier> `

Par exemple, pour compresser le fichier `fichier.txt` en utilisant l'algorithme **Huffman**, utilisez la commande suivante :

`python3 empaktor.py file.tar.gz --compression huffman  --compress fichier.txt `

Pour **décompresser** un fichier, utilisez la commande suivante :

`empaktor --decompress <fichier> [--compression <algorithme>]`

Par exemple, pour **décompresser** le fichier `fichier.txt.huffman` en utilisant l'algorithme **Huffman**, utilisez la commande suivante :

`empaktor --decompress fichier.txt.huffman --compression huffman`


## Compression

La compression des fichiers est effectuée en **deux étapes** :

* **Transformation des données** : les données sont transformées en utilisant l'algorithme de compression spécifié.

* **Encodage des données** : les données transformées sont encodées en utilisant un format compressé.

## Décompression

La décompression des fichiers est effectuée en **deux étapes** :

* **Décodage des données** : les données sont décodées à partir du format compressé.
* **Restauration des données** : les données décodées sont restaurées dans leur forme originale.


**Exemples**

Voici quelques exemples d'utilisation d'Empaktor :

* **Compresser un fichier texte :**
`empaktor --compress fichier.txt --compression huffman`

* **Compresser un fichier image :**
`empaktor --compress image.png --compression rle`

* **Compresser un fichier audio :**
`empaktor --compress musique.mp3 --compression bwt`

* **Décompresser un fichier compressé :**
`empaktor --decompress fichier.txt.huffman --compression huffman`

* **Décompresser un fichier compressé dans un dossier :**
`empaktor --decompress archive.tar.gz`


### Limitations

Empaktor a quelques **limitations** :

* Il ne prend en charge que les fichiers **texte**, **images** et **audio**.
* Il ne prend en charge que les algorithmes de compression **Huffman**, **RLE** et **BWT**.
* Il n'est pas optimisé pour la compression de **gros** fichiers.


### Améliorations possibles

Voici quelques **améliorations** possibles pour Empaktor :

* Prendre en charge d'autres types de fichiers, tels que les **fichiers vidéo** et les **fichiers binaires**.
* Prendre en charge d'autres algorithmes de compression, tels que l'algorithme **LZW**.
* Optimiser la **compression de gros fichiers**.
