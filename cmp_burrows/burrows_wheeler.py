def transform_bwt(data):

  # Construit une liste de toutes les rotations de la chaîne
  rotations = []
  for i in range(len(data)):
    rotations.append(data[i:] + data[:i])

  # Trie les rotations par ordre alphabétique
  rotations.sort()

  # Retourne la dernière colonne des rotations + la clé de transformation
  return rotations[-1], rotations.index(data)


def inverse_bwt(transformed_data, key):

  # Construit une liste de toutes les rotations de la chaîne transformée
  rotations = []
  for i in range(len(transformed_data)):
    rotations.append(transformed_data[i:] + transformed_data[:i])

  # Retourne la chaîne de caractères originale à partir de la clé de transformation
  return rotations[key]


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
