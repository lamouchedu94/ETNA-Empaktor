Transformation de Burrows-Wheeler (transform_bwt)

Prototype:
def transform_bwt(data: str) -> Tuple[str, int]:

Paramètres:
data (str): La chaîne de caractères à transformer.

Retour:
(str) La chaîne de caractères transformée.
(int) La clé de transformation.

Description:
Cette fonction applique la transformation de Burrows-Wheeler à la chaîne de caractères d'entrée data. La transformation réorganise les caractères de la chaîne en fonction d'une clé de transformation, créant ainsi la chaîne transformée. La fonction renvoie la chaîne transformée et la clé de transformation.

Exemple d'utilisation:
data = "banana"
transformed_data, key = transform_bwt(data)
Inverse de la Transformation de Burrows-Wheeler (inverse_bwt)

Prototype:
def inverse_bwt(transformed_data: str, key: int) -> str:

Paramètres:
transformed_data (str): La chaîne de caractères transformée.
key (int): La clé de transformation.

Retour:
(str) La chaîne de caractères inversée.

Description:

Cette fonction applique l'inverse de la transformation de Burrows-Wheeler à la chaîne transformée transformed_data en utilisant la clé de transformation key. Elle restaure la chaîne de caractères d'origine à partir de la chaîne transformée.

Exemple d'utilisation:

data = "banana"
transformed_data, key = transform_bwt(data)
original_data = inverse_bwt(transformed_data, key)