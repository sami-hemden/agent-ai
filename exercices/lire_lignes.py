with open("documents/rh.txt", "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()

print("Nombre de lignes :", len(lignes))

for numero, ligne in enumerate(lignes, start=1):
    print(numero, "-", ligne.strip())