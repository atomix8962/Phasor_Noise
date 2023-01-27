import os, runpy
from rsc.const import *


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

def explain() -> None:
    # Affichage de l'explication au démarrage
    os.system("cls|clear")
    for f in head:
        print(f)
    for f in explains:
        print(f)
    print()
    input("Press any key...")

def menu():
    explain()
    isRunning = True
    while isRunning == True:
        currentChoose = fileChooser()
        os.system("cls|clear")
        if currentChoose == "quit":
            print(bcolors.WARNING + "Exiting..." + bcolors.ENDC)
            isRunning = False
        else:
            runpy.run_module(mod_name=root[:-1] +"."+ currentChoose) # Run the currentChoose script

    print(bcolors.OKGREEN + "Done !" + bcolors.ENDC)
    print()

menu()