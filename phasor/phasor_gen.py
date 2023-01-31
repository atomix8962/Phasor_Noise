"""
Nom :           phasor/phasor_gen.py
Decription :    Script de calcul en un point du bruit Phasor
Date :          30/01/2023
Auteur :        Alexis
Statut :        Fonctionne en v1.0 (A faire relire par Alexis)
"""
"""
Informations gloabales du fichier:
Format des vecteurs : [x,y]
Format des noyaux : [position, direction, frequence, largeur]
"""

# Section des imports
# Math sert à utiliser les fonctions trigonométriques et exponentielles 
import math

# Section de définition des fonctions
"""
gaussian retourne le résultat du vecteur (vector) par la fonction gaussienne avec une largeur définie (bandwidth)
"""
def gaussian(vector:list, bandwidth:float) -> float:
    return math.exp(-math.pi*(bandwidth**2)*dot(vector, vector))

"""
dot retourne le produit scalaire entre deux vecteurs (vector1 et vector2)
"""
def dot(vector1: list, vector2: list) -> float:
    return vector1[0]*vector2[0]+vector1[1]*vector2[1]

"""
vector_subtraction retourne la soustraction de deux vecteurs (vector1 et vector2)
"""
def vector_subtraction(vector1: list, vector2: list) -> list:
    return [vector1[0]-vector2[0], vector1[1]-vector2[1]]

"""
polar_coordinates_coefficients retourne la somme des coordonnées polaires des vecteurs (A vérifier par Alexis)
"""
def polar_coordinates_coefficients(x: list, kernel_array: list) -> list:
    return [gaussian(vector_subtraction(x, kernel[0]), kernel[3]) * math.sin(-dot(vector_subtraction(x, kernel[0]), kernel[1]) * kernel[2]) for kernel in kernel_array],\
           [gaussian(vector_subtraction(x, kernel[0]), kernel[3]) * math.cos(-dot(vector_subtraction(x, kernel[0]), kernel[1]) * kernel[2]) for kernel in kernel_array]

"""
phase_func retourne la phase du bruit calculé
"""
def phase_func(x: list, kernel_array: list) -> float:
    l1, l2 = polar_coordinates_coefficients(x, kernel_array)
    return math.atan2(sum(l1), sum(l2))

"""
phasor_noise retourne le sinus de la phase du bruit calculé 
"""
def phasor_noise(x: list, kernel_array: list) -> float:
    return math.sin(phase_func(x, kernel_array))