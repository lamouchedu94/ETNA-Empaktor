import argparse
import tarfile
import os
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
        with tarfile.open(file_name, "r:gz") as archive:
            for member in archive.getmembers():
                if member.isfile() and member.name.endswith(".huffman"):
                    file_data = archive.extractfile(member).read().decode()
                    decoded_data = huffman.decompress_huffman(file_data)
                    output_file_name = os.path.join(os.path.dirname(file_name), member.name)
                    with open(output_file_name.replace(".huffman", ".txt"), "w") as decompressed_file:
                        decompressed_file.write(decoded_data)
                    print("Décompression terminée. Fichier décompressé : " + output_file_name.replace(".huffman", ".txt"))
    elif algorithm == "rle":
        with tarfile.open(file_name, "r:gz") as archive:
            for member in archive.getmembers():
                if member.isfile() and member.name.endswith(".rle"):
                    file_data = archive.extractfile(member).read().decode()
                    decoded_data = rle.decode_rle(file_data)
                    output_file_name = os.path.join(os.path.dirname(file_name), member.name)
                    with open(output_file_name.replace(".rle", ".txt"), "w") as decompressed_file:
                        decompressed_file.write(decoded_data)
                    print("Décompression terminée. Fichier décompressé : " + output_file_name.replace(".rle", ".txt"))
    elif algorithm == "bwt":
        with tarfile.open(file_name, "r:gz") as archive:
            for member in archive.getmembers():
                if member.isfile() and member.name.endswith(".bwt"):
                    file_data = archive.extractfile(member).read().decode()
                    with open(file_name + ".key", "r") as key_file:
                        key = int(key_file.read())
                    original_data = inverse_bwt(file_data, key)
                    output_file_name = os.path.join(os.path.dirname(file_name), member.name)
                    with open(output_file_name.replace(".bwt", ".txt"), "w") as decompressed_file:
                        decompressed_file.write(original_data)
                    print("Décompression terminée. Fichier décompressé : " + output_file_name.replace(".bwt", ".txt"))
    else:
        print("Algorithme de compression non pris en charge : " + algorithm)

# Fonction pour décompresser un fichier
def extract_files(archive_name):
    with tarfile.open(archive_name, "r:gz") as archive:
        archive.extractall()

        # décompresser chaque fichier extrait en utilisant la fonction decompress_file
        for file_name in archive.getnames():
            if file_name.endswith(".huffman"):
                decompress_file(file_name, "huffman")
            elif file_name.endswith(".rle"):
                decompress_file(file_name, "rle")
            elif file_name.endswith(".bwt"):
                decompress_file(file_name, "bwt")
                

# Parser d'arguments en ligne de commande
parser = argparse.ArgumentParser(
    description="Empaktor - Compression et décompression de fichiers"
)
parser.add_argument("archive", help="Nom de l'archive compressée")
parser.add_argument("--extract", action="store_true", help="Extraire un fichier compressé")
parser.add_argument(
    "--compression", choices=["huffman", "rle", "bwt"], help="Algorithme de compression"
)
parser.add_argument("--compress", nargs="+", help="Fichiers à compresser")
parser.add_argument("--decompress", nargs="*", help="Fichiers à décompresser")

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
    for algo in ["huffman", "rle", "bwt"]:
        decompress_file(args.archive, algo)
    print(f"Décompression terminée. Fichiers extraits.")
else:
    print("L'argument --extract est requis pour la décompression. Spécifiez l'algorithme de compression utilisé.")