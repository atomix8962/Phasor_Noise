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

class PhasorGenerator:
    """
    Classe inutilisable dans l'état doit redéfinir:
     -exp
     -sin
     -cos
     -atan2
     -dot
     -vector_subtraction
     Aller voir l'implémentation:
     -Python : phasor_py.py
     -Numpy : phasor_numpy.py
     -Jax : phasor_jax.py
    """

    def __init__(self):
        pass

    def exp(self, x):
        """
            La fonction exponentielle
        """
        raise NotImplemented()

    def sin(self, x):
        """
            La fonction sinus
        """
        raise NotImplemented()

    def cos(self, x):
        """
            La fonction cosinus
        """
        raise NotImplemented()

    def atan2(self, x, y):
        """
            La fonction atan2
        """
        raise NotImplemented()

    def dot(self, v1, v2):
        """
        dot retourne le produit scalaire entre deux vecteurs (vector1 et vector2)
        """
        raise NotImplemented()

    def vector_subtraction(self, vector1: list, vector2: list):
        """
        vector_subtraction retourne la soustraction de deux vecteurs (vector1 et vector2)
        """
        raise NotImplemented()

    def gaussian(self, vector:list, bandwidth:float) -> float:
        """
        gaussian retourne le résultat du vecteur (vector) par la fonction gaussienne avec une largeur définie (bandwidth)
        """
        return self.exp(-math.pi*(bandwidth**2)*self.dot(vector, vector))

    def polar_coordinates_coefficients(self, x: list, kernel_array: list) -> list:
        """
        polar_coordinates_coefficients retourne la somme des coordonnées polaires des vecteurs (A vérifier par Alexis)
        """
        return [self.gaussian(self.vector_subtraction(x, kernel[0]), kernel[3]) * self.sin(
            -self.dot(self.vector_subtraction(x, kernel[0]), kernel[1]) * kernel[2]) for kernel in kernel_array], \
               [self.gaussian(self.vector_subtraction(x, kernel[0]), kernel[3]) * self.cos(
                   -self.dot(self.vector_subtraction(x, kernel[0]), kernel[1]) * kernel[2]) for kernel in kernel_array]

    def phase_func(self, x: list, kernel_array: list) -> float:
        """
        phase_func retourne la phase du bruit calculé
        """
        l1, l2 = self.polar_coordinates_coefficients(x, kernel_array)
        return self.atan2(sum(l1), sum(l2))

    def phasor_noise(self, x: list, kernel_array: list) -> float:
        """
            phasor_noise retourne le sinus de la phase du bruit calculé
        """
        return self.sin(self.phase_func(x, kernel_array))

def timeperf(func):
    def inner(*args, **kargs):
        import time
        begin = time.perf_counter_ns()
        result = func(*args, **kargs)
        end = time.perf_counter_ns()
        return result, end-begin
    return inner
