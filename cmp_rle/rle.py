import argparse


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
    decoded_data = ""
    count = ""
    for char in encoded_data:
        if char.isdigit():
            count += char
        else:
            decoded_data += char * int(count)
            count = ""
    return decoded_data
