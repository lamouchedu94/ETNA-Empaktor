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


def compress_file(filename, compression_algorithm):
    with open(filename, "r") as file:
        data = file.read()
        if compression_algorithm == "rle":
            encoded_data = encode_rle(data)
            with open(filename + ".rle", "w") as compressed_file:
                compressed_file.write(encoded_data)


def decompress_file(filename, compression_algorithm):
    if compression_algorithm == "rle":
        with open(filename, "r") as file:
            encoded_data = file.read()
            decoded_data = decode_rle(encoded_data)
            with open(filename + ".decoded", "w") as decompressed_file:
                decompressed_file.write(decoded_data)


def main():
    parser = argparse.ArgumentParser(
        description="Empaktor: Compression and Decompression Tool"
    )
    parser.add_argument("file", help="Input file for compression or decompression")
    parser.add_argument(
        "--compression", help="Compression algorithm (e.g., rle, huffman, bwt)"
    )
    parser.add_argument(
        "--extract", action="store_true", help="Extract compressed file"
    )

    args = parser.parse_args()

    if args.extract:
        decompress_file(args.file, args.compression)
        print("File decompressed successfully.")
    else:
        compress_file(args.file, args.compression)
        print("File compressed successfully.")


if __name__ == "__main__":
    main()
