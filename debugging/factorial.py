#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un nombre entier positif ou nul.

    Paramètre:
        n (int): Nombre dont on veut calculer la factorielle

    Retour:
        int: Factorielle de n
    """
    result = 1
    while n > 1:
        result *= n  # Multiplie le résultat par n
        n -= 1       # Décrémente n pour éviter la boucle infinie
    return result

if __name__ == "__main__":
    # Vérifie qu'un argument a été passé
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <nombre_entier>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Le nombre doit être positif ou nul.")
    except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
    
    f = factorial(number)
    print(f)
