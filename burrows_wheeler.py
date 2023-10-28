import argparse
import os


def transform_bwt(data):
    data += "\0"  # Ajouter un caractère de fin unique
    rotations = sorted([data[i:] + data[:i] for i in range(len(data))])
    transformed_data = "".join(rot[-1] for rot in rotations)
    key = rotations.index(data)
    return transformed_data, key


def inverse_bwt(transformed_data, key):
    table = sorted([c for c in transformed_data])
    original_data = [""] * len(transformed_data)

    for i in range(len(transformed_data)):
        table = sorted(
            [transformed_data[j] + table[j] for j in range(len(transformed_data))]
        )
        original_data[i] = table[key]

    result = [s for s in original_data if s.endswith("\0")][0]
    return result.rstrip("\0")


def compress_file(file_name, algorithm):
    with open(file_name, "r") as file:
        data = file.read()
        if algorithm == "bwt":
            transformed_data, key = transform_bwt(data)
            # Sauvegardez la clé dans un fichier séparé pour la décompression
            with open(file_name + ".key", "w") as key_file:
                key_file.write(str(key))
            # Sauvegardez les données transformées
            with open(file_name + ".bwt", "w") as transformed_file:
                transformed_file.write(transformed_data)
            return transformed_data
        else:
            raise ValueError(
                "Algorithme de compression non pris en charge : " + algorithm
            )


def decompress_file(file_name, algorithm):
    if algorithm == "bwt":
        # Chargez la clé depuis le fichier
        with open(file_name + ".key", "r") as key_file:
            key = int(key_file.read())
        # Chargez les données transformées
        with open(file_name + ".bwt", "r") as transformed_file:
            transformed_data = transformed_file.read()
        original_data = inverse_bwt(transformed_data, key)
        with open(file_name + ".decoded", "w") as decoded_file:
            decoded_file.write(original_data)
        print("Décompression terminée. Fichier décompressé : " + file_name + ".decoded")
    else:
        raise ValueError("Algorithme de compression non pris en charge : " + algorithm)


def main():
    parser = argparse.ArgumentParser(
        description="Empaktor: Compression and Decompression Tool"
    )
    parser.add_argument(
        "file", help="Fichier d'entrée pour la compression ou la décompression"
    )
    parser.add_argument(
        "--compression", help="Algorithme de compression (par exemple, bwt)"
    )
    parser.add_argument(
        "--extract", action="store_true", help="Extraire un fichier compressé"
    )

    args = parser.parse_args()

    if args.extract:
        decompress_file(args.file, args.compression)
    else:
        compress_file(args.file, args.compression)


if __name__ == "__main__":
    main()
