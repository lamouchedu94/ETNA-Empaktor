def transform_bwt(data):

    data += '\0'  # Ajouter un caractère de fin unique
    rotations = sorted([data[i:] + data[:i] for i in range(len(data))])
    transformed_data = ''.join(rot[-1] for rot in rotations)
    key = rotations.index(data)
    return transformed_data, key

def inverse_bwt(transformed_data, key):

    table = sorted([c for c in transformed_data])
    original_data = [''] * len(transformed_data)
    
    for i in range(len(transformed_data)):
        table = sorted([transformed_data[j] + table[j] for j in range(len(transformed_data))])
        original_data[i] = table[key]
    
    result = [s for s in original_data if s.endswith('\0')][0]
    return result.rstrip('\0')

if __name__ == "__main__":

    data = "banana"
    transformed_data, key = transform_bwt(data)
    original_data = inverse_bwt(transformed_data, key)
    print("Exemple 1:")
    print("Données d'origine:", data)
    print("Transformée de Burrows-Wheeler:", transformed_data)
    print("Données inversées:", original_data)
    print()

    data = "hello"
    transformed_data, key = transform_bwt(data)
    original_data = inverse_bwt(transformed_data, key)
    print("Exemple 2:")
    print("Données d'origine:", data)
    print("Transformée de Burrows-Wheeler:", transformed_data)
    print("Données inversées:", original_data)
    print()
