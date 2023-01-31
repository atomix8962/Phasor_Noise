"""
Nom :           main.py
Decription :    Script principal du projet "Phasor Noise Generator"
Date :          30/01/2023
Auteur :        Paul B.
Statut :        Fonctionne en v1.0 (vérifié & relu)
"""

# Section des imports
# os sert a effacer le terminal pour l'affichage du générateur et de récupérer les fichiers du dossier root/
import os
# runpy permet d'éxécuter un script python (on s'en servira ici pour exécuter les scripts du dossier root/)
import runpy 
# rsc.const permet d'accéder à toutes les constantes du projet
from rsc.const import *

# Section de définition des fonctions
"""
fileChooser est un script qui permet d'afficher un séléctionneur de script a éxécuter du dossier root/
par défaut, on ne met pas d'erreur, la fonction s'appelera récursivement si une erreur se produit
"""
def fileChooser(error:str=None) -> str:
    # On parcourt les fichiers du dossier root qui contient tous les scripts
    files = [f.split(".")[:-1] for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]

    # Affichage dans le terminal
    os.system("cls|clear")
    for f in head:
        print(f)
    for i in range(len(files)):
        print(f"{i}- {files[i][0]}")
    print(f"{len(files)}- QUIT")
    print()
    if error != None:
        print(bcolors.FAIL + error + bcolors.ENDC)
    choice = input("->")

    # Vérification de la validité de l'entrée
    try :
        if int(choice) < len(files) and int(choice) >= 0:
            return files[int(choice)][0]
        if int(choice) == len(files):
            return "quit"
    except:
        return fileChooser("An error occured...")

"""
explain permet d'afficher un petit texte explicatif du projet au premier démarrage du script
"""
def explain() -> None:
    # Affichage de l'explication au démarrage
    os.system("cls|clear")
    for f in head:
        print(f)
    for f in explains:
        print(f)
    print()
    input("Press any key...")

"""
menu est la fonction qui gère l'ensemble du script de main.py
"""
def menu() -> None:
    explain()
    isRunning = True
    while isRunning == True:
        currentChoose = fileChooser()
        os.system("cls|clear")
        if currentChoose == "quit":
            print("Exiting...")
            isRunning = False
        else:
            runpy.run_module(mod_name=root[:-1] +"."+ currentChoose) # Execute le script choisi
    os.system("cls|clear")
    print(bcolors.OKGREEN + "Done !" + bcolors.ENDC)
    print()

# Section du script
if __name__== "__main__":
    menu() # On démarre le menu du projet