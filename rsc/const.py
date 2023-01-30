"""
Nom :           rsc/const.py
Decription :    Déclaration des constantes du projet
Date :          30/01/2023
Auteur :        Paul BEDROSSIAN
Statut :        Fonctionne en v1.0 (vérifié & relu)
"""

# Chemins d'accès
root = "root/"

# Couleurs textuelles dans le terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Texte à afficher (pour le menu textuelle)
head = [
    bcolors.HEADER +
    "--------------------------------",
    "---  Phasor Noise Generator  ---",
    "--------------------------------" +
    bcolors.ENDC,
    ""
]

explains = [
    "-> Explanation here............." 
]

