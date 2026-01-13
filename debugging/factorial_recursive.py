#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculer la factorielle d'un entier naturel n.

    Description :
        Cette fonction utilise la récursion pour calculer la factorielle d'un entier n.
        La factorielle de n (notée n!) est le produit de tous les entiers positifs de 1 à n.
        Par définition, 0! = 1.

    Paramètres :
        n (int) : Un entier naturel dont on souhaite calculer la factorielle.

    Retour :
        int : La factorielle de l'entier donné n.
    """
    if n == 0:            # Cas de base : 0! = 1
        return 1
    else:
        return n * factorial(n-1)  # Cas récursif : n! = n * (n-1)!

# Lecture du premier argument passé en ligne de commande,
# conversion en entier, et calcul de sa factorielle
f = factorial(int(sys.argv[1]))

# Affichage du résultat
print(f)
