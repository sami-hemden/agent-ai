with open("documents/rh.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()

print(contenu)
print("Nombre de caractères :", len(contenu))