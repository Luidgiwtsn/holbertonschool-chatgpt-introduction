#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un entier naturel n de manière récursive.

    Args:
        n (int): Entier naturel dont on souhaite calculer la factorielle.

    Returns:
        int: La factorielle de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Récupère l'entier passé en argument, calcule sa factorielle, puis affiche le résultat
f = factorial(int(sys.argv[1]))
print(f)