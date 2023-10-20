def encode_rle(data):
    # Initialise une chaîne vide pour stocker les données encodées
    encoded_data = ""
    # Initialise la première lettre de la chaîne en cours et le compteur
    current_char = data[0]
    count = 1

    # Parcourt chaque lettre à partir de la deuxième lettre
    for char in data[1:]:
        # Si la lettre est identique à la lettre en cours, incrémente le compteur
        if char == current_char:
            count += 1
        else:
            # Si la lettre est différente, ajoute le nombre d'occurrences (count) suivi de la lettre en cours à la chaîne encodée
            encoded_data += str(count) + current_char
            # Met à jour la lettre en cours et réinitialise le compteur à 1
            current_char = char
            count = 1

    # Ajoute le dernier groupe de caractères à la chaîne encodée
    encoded_data += str(count) + current_char

    return encoded_data

def decode_rle(encoded_data):
    # Initialise une chaîne vide pour stocker les données décodées
    decoded_data = ""
    # Initialise un index pour parcourir la chaîne encodée
    i = 0

    # Parcourt la chaîne encodée
    while i < len(encoded_data):
        count = ""
        # Tant que le caractère en cours est un chiffre (pour représenter le compteur)
        while i < len(encoded_data) and encoded_data[i].isdigit():
            # Ajoute le chiffre à la variable "count"
            count += encoded_data[i]
            i += 1
        # Le caractère suivant après les chiffres est le caractère à répéter
        char = encoded_data[i]
        # Ajoute le caractère répété "count" fois à la chaîne décodée
        decoded_data += char * int(count)
        i += 1

    return decoded_data


    # Exemple 1


data = "AAABBBCCD"
encoded_data = encode_rle(data)
decoded_data = decode_rle(encoded_data)
print("Exemple 1:")
print("Données d'origine:", data)
print("Données encodées:", encoded_data)
print("Données décodées:", decoded_data)
print()

# Exemple 2
data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
encoded_data = encode_rle(data)
decoded_data = decode_rle(encoded_data)
print("Exemple 2:")
print("Données d'origine:", data)
print("Données encodées:", encoded_data)
print("Données décodées:", decoded_data)
print()
