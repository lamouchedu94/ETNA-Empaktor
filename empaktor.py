import argparse
import tarfile
import tempfile
import huffman
import rle
from burrows_wheeler import transform_bwt, inverse_bwt


# Fonction pour compresser un fichier
def compress_file(file_name, algorithm):
    with open(file_name, "r") as file:
        data = file.read()
        if algorithm == "huffman":
            codee, dico = huffman.compress_huffman(data)
            return codee
        elif algorithm == "rle":
            encoded_data = rle.encode_rle(data)
            return encoded_data
        elif algorithm == "bwt":
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


# Fonction pour décompresser un fichier
def decompress_file(file_name, algorithm):
    if algorithm == "huffman":
        return huffman.decompress_huffman(file_name)
    elif algorithm == "rle":
        return rle.decode_rle(file_name)
    elif algorithm == "bwt":
        # Chargez la clé depuis le fichier
        with open(file_name + ".key", "r") as key_file:
            key = int(key_file.read())
        # Chargez les données transformées
        with open(file_name + ".bwt", "r") as transformed_file:
            transformed_data = transformed_file.read()
        original_data = inverse_bwt(transformed_data, key)
        # Renommez le fichier décompressé avec l'extension appropriée
        with open(file_name + ".decoded", "w") as decoded_file:
            decoded_file.write(original_data)
        print("Décompression terminée. Fichier décompressé : " + file_name + ".decoded")
    else:
        raise ValueError("Algorithme de compression non pris en charge : " + algorithm)


# Parser d'arguments en ligne de commande
parser = argparse.ArgumentParser(
    description="Empaktor - Compression et décompression de fichiers"
)
parser.add_argument("archive", help="Nom de l'archive compressée")
parser.add_argument(
    "--compression", choices=["huffman", "rle", "bwt"], help="Algorithme de compression"
)
parser.add_argument("--compress", nargs="+", help="Fichiers à compresser")
parser.add_argument("--decompress", nargs="*", help="Fichiers à décompresser")
parser.add_argument(
    "--extract", action="store_true", help="Extraire un fichier compressé"
)

args = parser.parse_args()

if args.compression and args.compress:
    # Compression des fichiers
    archive_name = args.archive
    with tarfile.open(archive_name, "w:gz") as archive:
        for file_name in args.compress:
            compressed_data = compress_file(file_name, args.compression)
            with tempfile.NamedTemporaryFile(mode="wb", delete=False) as temp_file:
                temp_file.write(
                    compressed_data.encode()
                )  # Écrire les données compressées dans le fichier temporaire
            archive.add(temp_file.name, arcname=file_name)

    print(f"Compression terminée. Archive créée : {archive_name}")
elif args.extract:
    # Décompression des fichiers si --extract est activé
    archive_name = args.archive
    with tarfile.open(archive_name, "r:gz") as archive:
        archive.extractall()
        print(f"Décompression terminée. Fichiers extraits.")
elif args.compression and args.decompress:
    # Décompression des fichiers spécifiques
    for file_name in args.decompress:
        decompress_file(file_name, args.compression)
else:
    print(
        "Aucune action spécifiée. Utilisez --compression pour compresser, --decompress pour décompresser ou --extract pour extraire un fichier compressé."
    )
