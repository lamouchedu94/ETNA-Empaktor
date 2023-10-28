import argparse
import math

def occurence(chaine):
    dico = {}
    for car in chaine:
        if car in dico:
            dico[car] += 1
        else:
            dico[car] = 1
    return dico

def tri(dico):
    res = []
    while len(dico) > 0:
        max_occu = -math.inf
        car_min = ""
        for occu in dico:
            if dico[occu] > max_occu:
                max_occu = dico[occu]
                car_min = occu
        res.append((car_min, dico[car_min]))
        del dico[car_min]
    return res

def n(dico):
    tab_noeud = tri(dico)
    while len(tab_noeud) > 1:
        derniers = ((tab_noeud[-1], tab_noeud[-2]), tab_noeud[-1][1] + tab_noeud[-2][1])
        poid_derniers = derniers[1]
        tab_noeud = tab_noeud[0:len(tab_noeud) - 2]
        trouve = False
        for i in range(len(tab_noeud)):
            if poid_derniers > tab_noeud[i][1]:
                temp = tab_noeud[0:i]
                temp.append(derniers)
                temp += tab_noeud[i:len(tab_noeud)]
                tab_noeud = temp
                trouve = True
                break
        if not trouve:
            tab_noeud.append(derniers)
    return tab_noeud

def codage(noeud, res, chemin):
    if type(noeud[0]) == str:
        res[noeud[0]] = chemin
        return
    codage(noeud[0][0], res, chemin + "0")
    codage(noeud[0][1], res, chemin + "1")

def encode(tab, chaine):
    res = {}
    codage(tab[0], res, "")
    codee = ""
    for car in chaine:
        codee += res[car]
    return codee, res

def decode(codee, dico):
    enclair = ""
    while len(codee) > 0:
        for cles in dico:
            if codee.startswith(dico[cles]):
                enclair += cles
                codee = codee[len(dico[cles]):]
    return enclair

def initialize_dico(chaine):
    dico = {}
    for car in chaine:
        if car in dico:
            dico[car] += 1
        else:
            dico[car] = 1
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ .,()":
        if char not in dico:
            dico[char] = 0
    return dico

def compress_huffman(chaine):
    dico = initialize_dico(chaine)
    tab = n(dico)
    codee, dico = encode(tab, chaine)
    return codee, dico

def decompress_huffman(codee, dico):
    return decode(codee, dico)

def compress_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        compressed_data, dico = compress_huffman(data)
        with open(filename + '.huffman', 'w') as compressed_file:
            compressed_file.write(compressed_data)
        # Sauvegardez le dictionnaire pour pouvoir le réutiliser lors de la décompression
        with open(filename + '.huffman.dico', 'w') as dico_file:
            for key, value in dico.items():
                dico_file.write(f"{key}:{value}\n")

def decompress_file(filename):
    if filename.endswith('.huffman'):
        # Chargez le dictionnaire
        dico = {}
        with open(filename + '.dico', 'r') as dico_file:
            for line in dico_file:
                key, value = line.strip().split(':')
                dico[key] = value
        with open(filename, 'r') as file:
            encoded_data = file.read()
            decoded_data = decompress_huffman(encoded_data, dico)
            with open(filename + '.decoded', 'w') as decompressed_file:
                decompressed_file.write(decoded_data)
    else:
        print("Fichier non compressé avec Huffman")

def main():
    parser = argparse.ArgumentParser(description="Empaktor: Compression and Decompression Tool")
    parser.add_argument("file", help="Input file for compression or decompression")
    parser.add_argument("--compression", help="Compression algorithm (e.g., rle, huffman, bwt)")
    parser.add_argument("--extract", action="store_true", help="Extract compressed file")

    args = parser.parse_args()

    if args.extract:
        decompress_file(args.file)
        print("File decompressed successfully.")
    else:
        compress_file(args.file)
        print("File compressed successfully.")

if __name__ == "__main__":
    main()
