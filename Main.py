import os
import shutil

def organiser_fichiers_par_extension(dossier):
    # Liste tous les fichiers et dossiers dans 'dossier'
    fichiers = os.listdir(dossier)

    for nom in fichiers:
        chemin_complet = os.path.join(dossier, nom)

        # On vérifie que c'est un fichier (pas un dossier)
        if os.path.isfile(chemin_complet):
            # Récupère l'extension avec le point, ex ".jpg"
            _, extension = os.path.splitext(nom)

            # On enlève le point et passe en minuscules, ex "jpg"
            extension = extension[1:].lower()

            # Si le fichier n'a pas d'extension, on le met dans "SansExtension"
            if extension == "":
                extension = "SansExtension"

            # Crée le chemin du dossier cible pour cette extension
            dossier_cible = os.path.join(dossier, extension)

            # Crée le dossier s'il n'existe pas
            os.makedirs(dossier_cible, exist_ok=True)

            # Déplace le fichier dans ce dossier
            shutil.move(chemin_complet, os.path.join(dossier_cible, nom))

            print(f"Déplacé : {nom} -> {extension}/")

# Demande le chemin au lancement
chemin = input("Chemin du dossier à organiser : ")
organiser_fichiers_par_extension(chemin)