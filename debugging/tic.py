#!/usr/bin/python3
def afficher_plateau(plateau):
    """
    Affiche le plateau de jeu.

    Args:
        plateau (list[list[str]]): Le plateau de 3x3 contenant "X", "O" ou " ".
    """
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * (len(ligne)*4 - 1))


def verifier_victoire(plateau):
    """
    Vérifie si un joueur a gagné.

    Args:
        plateau (list[list[str]]): Le plateau de jeu.

    Returns:
        bool: True si un joueur a gagné, False sinon.
    """
    # Vérification des lignes
    for ligne in plateau:
        if ligne.count(ligne[0]) == len(ligne) and ligne[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(plateau[0])):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] and plateau[0][col] != " ":
            return True

    # Vérification des diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] and plateau[0][0] != " ":
        return True

    if plateau[0][2] == plateau[1][1] == plateau[2][0] and plateau[0][2] != " ":
        return True

    return False


def plateau_plein(plateau):
    """
    Vérifie si le plateau est plein (match nul).

    Args:
        plateau (list[list[str]]): Le plateau de jeu.

    Returns:
        bool: True si le plateau est plein, False sinon.
    """
    for ligne in plateau:
        if " " in ligne:
            return False
    return True


def morpion():
    """
    Lance le jeu du Morpion (Tic-Tac-Toe) en console.
    Deux joueurs s'affrontent en plaçant alternativement "X" et "O".
    """
    plateau = [[" "]*3 for _ in range(3)]
    joueur = "X"

    while True:
        afficher_plateau(plateau)

        # Boucle de saisie avec validation
        while True:
            try:
                ligne = int(input(f"Entrez la ligne (0, 1 ou 2) pour le joueur {joueur} : "))
                colonne = int(input(f"Entrez la colonne (0, 1 ou 2) pour le joueur {joueur} : "))
                if ligne not in [0, 1, 2] or colonne not in [0, 1, 2]:
                    print("Entrée invalide ! La ligne et la colonne doivent être 0, 1 ou 2.")
                elif plateau[ligne][colonne] != " ":
                    print("Cette case est déjà prise ! Réessayez.")
                else:
                    break
            except ValueError:
                print("Entrée invalide ! Veuillez entrer des nombres.")

        plateau[ligne][colonne] = joueur

        if verifier_victoire(plateau):
            afficher_plateau(plateau)
            print(f"Le joueur {joueur} a gagné !")
            break

        if plateau_plein(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        # Changement de joueur
        joueur = "O" if joueur == "X" else "X"


# Lancer le jeu
morpion()
