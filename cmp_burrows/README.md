# Transformée de Burrows-Wheeler

## Introduction

La transformée de Burrows-Wheeler est une transformation d'une chaîne de caractères en une autre chaîne de caractères, qui préserve l'ordre des suffixes de la chaîne originale.

### Algorithme
L'algorithme de la transformée de Burrows-Wheeler est le suivant :

* On ajoute un caractère de fin unique à la chaîne de caractères originale.
* On trie les rotations de la chaîne de caractères, c'est-à-dire les chaînes obtenues en faisant pivoter la chaîne originale d'un certain nombre de positions.
* On prend le dernier caractère de chaque rotation.
* On renvoie la chaîne composée de ces caractères.

**Prototype**
```
def transform_bwt(data):
    """
    Transforme une chaîne de caractères en sa transformée de Burrows-Wheeler.

    Args:
        data: La chaîne de caractères à transformer.

    Returns:
        La transformée de Burrows-Wheeler de la chaîne de caractères.
    """
```

### Paramètres

* data : La chaîne de caractères à transformer.


### Retour

* La transformée de Burrows-Wheeler de la chaîne de caractères.

**Exemple d'utilisation**
```
>from burrows_wheeler import transform_bwt, inverse_bwt

# Exemple 1
data = "banana"
transformed_data, key = transform_bwt(data)
original_data = inverse_bwt(transformed_data, key)
print("Exemple 1:")
print("Données d'origine:", data)
print("Transformée de Burrows-Wheeler:", transformed_data)
print("Données inversées:", original_data)
print()

```

## Description

L'algorithme de **la transformée de Burrows-Wheeler** fonctionne en triant les rotations de la chaîne de caractères originale. Les rotations sont triées en fonction de leur dernier caractère. Le résultat de ce tri est une chaîne de caractères composée des derniers caractères de chaque rotation.

**La transformée de Burrows-Wheeler** est une transformation réversible. Il est possible de retrouver la chaîne originale à partir de sa transformée en utilisant l'algorithme inverse de la transformée de Burrows-Wheeler.

## Algorithme inverse
L'algorithme inverse de la transformée de Burrows-Wheeler est le suivant :

* On trie la transformée de Burrows-Wheeler.
* On construit une table contenant les positions de chaque caractère dans la chaîne originale.
* On insère les caractères de la transformée de Burrows-Wheeler dans la chaîne originale, en utilisant la table pour déterminer la position de chaque caractère.

**Prototype**
```
def inverse_bwt(transformed_data, key):
    """
    Inverse la transformée de Burrows-Wheeler d'une chaîne de caractères.

    Args:
        transformed_data: La transformée de Burrows-Wheeler de la chaîne de caractères.
        key: La position de la chaîne de caractères originale dans les rotations.

    Returns:
        La chaîne de caractères originale.
    """
```

## Paramètres

`transformed_data` : La transformée de Burrows-Wheeler de la chaîne de caractères.
`key` : La position de la chaîne de caractères originale dans les rotations.

=> Retourne la chaîne de caractère originale.

**Exemple d'utilisation**
```
# Exemple 2
data = "hello"
transformed_data, key = transform_bwt(data)
original_data = inverse_bwt(transformed_data, key)
print("Exemple 2:")
print("Données d'origine:", data)
print("Transformée de Burrows-Wheeler:", transformed_data)
print("Données inversées:", original_data)
print()
```

## Description

L'algorithme inverse de **la transformée de Burrows-Wheeler** fonctionne en triant la transformée de Burrows-Wheeler. Une fois la transformée de Burrows-Wheeler triée, on peut reconstruire la chaîne originale en insérant les caractères de la transformée de Burrows-Wheeler dans la chaîne originale, en utilisant une table pour déterminer la position de chaque caractère.

La table est construite en triant la transformée de Burrows-Wheeler et en stockant la position de chaque caractère dans la chaîne originale.
