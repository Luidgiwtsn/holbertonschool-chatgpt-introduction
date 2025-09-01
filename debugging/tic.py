def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 5)

def verifier_gagnant(plateau):
    # Vérifier les lignes
    for ligne in plateau:
        if ligne.count(ligne[0]) == 3 and ligne[0] != " ":
            return True

    # Vérifier les colonnes
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] and plateau[0][col] != " ":
            return True

    # Vérifier les diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] and plateau[0][0] != " ":
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] and plateau[0][2] != " ":
        return True

    return False

def match_nul(plateau):
    for ligne in plateau:
        if " " in ligne:
            return False
    return True

def morpion():
    plateau = [[" "]*3 for _ in range(3)]
    joueur = "X"

    while True:
        afficher_plateau(plateau)

        try:
            ligne = int(input(f"Joueur {joueur}, entrez la ligne (0, 1 ou 2) : "))
            colonne = int(input(f"Joueur {joueur}, entrez la colonne (0, 1 ou 2) : "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres entre 0 et 2.")
            continue

        if not (0 <= ligne <= 2 and 0 <= colonne <= 2):
            print("Coordonnées hors limites. Veuillez entrer des nombres entre 0 et 2.")
            continue

        if plateau[ligne][colonne] != " ":
            print("Cette case est déjà prise ! Essayez encore.")
            continue

        plateau[ligne][colonne] = joueur

        if verifier_gagnant(plateau):
            afficher_plateau(plateau)
            print(f"Félicitations ! Le joueur {joueur} a gagné !")
            break

        if match_nul(plateau):
            afficher_plateau(plateau)
            print("Match nul ! Aucun gagnant.")
            break

        joueur = "O" if joueur == "X" else "X"

morpion()