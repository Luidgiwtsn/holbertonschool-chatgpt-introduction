#!/usr/bin/python3
import random
import os


def clear_screen():
    """
    Efface l'écran du terminal.

    Utilise la commande appropriée selon le système d'exploitation :
    - 'cls' pour Windows
    - 'clear' pour Unix/Linux/macOS
    """
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    """
    Classe représentant le jeu du Démineur en mode console.
    """

    def __init__(self, width=10, height=10, mines=10):
        """
        Initialise une nouvelle partie de Démineur.

        :param width: largeur du plateau (nombre de colonnes)
        :param height: hauteur du plateau (nombre de lignes)
        :param mines: nombre total de mines
        """
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        """
        Affiche le plateau de jeu dans le terminal.

        :param reveal: si True, toutes les cases sont révélées
                       (utilisé à la fin de la partie)
        """
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        """
        Compte le nombre de mines adjacentes à une case donnée.

        :param x: coordonnée x de la case
        :param y: coordonnée y de la case
        :return: nombre de mines autour de la case
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """
        Révèle une case du plateau.

        Si la case contient une mine, la partie est perdue.
        Si la case ne contient aucune mine adjacente, les cases
        voisines sont révélées récursivement.

        :param x: coordonnée x de la case
        :param y: coordonnée y de la case
        :return: False si une mine est déclenchée, True sinon
        """
        if self.revealed[y][x]:
            return True

        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        """
        Vérifie si la condition de victoire est atteinte.

        Le joueur gagne lorsque toutes les cases sans mine
        ont été révélées.

        :return: True si la partie est gagnée, False sinon
        """
        revealed_cells = sum(
            self.revealed[y][x]
            for y in range(self.height)
            for x in range(self.width)
        )
        return revealed_cells == (self.width * self.height - len(self.mines))

    def play(self):
        """
        Lance la boucle principale du jeu.

        Gère l'affichage, les entrées utilisateur,
        la détection de défaite et de victoire.
        """
        while True:
            self.print_board()
            try:
                x = int(input("Coordonnée x : "))
                y = int(input("Coordonnée y : "))

                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordonnées hors limites.")
                    input("Appuyez sur Entrée...")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("💥 Perdu ! Vous avez déclenché une mine.")
                    break

                if self.check_win():
                    self.print_board(reveal=True)
                    print("🎉 Bravo ! Vous avez gagné !")
                    break

            except ValueError:
                print("Entrée invalide. Veuillez entrer des nombres.")
                input("Appuyez sur Entrée...")


if __name__ == "__main__":
    """
    Point d’entrée du programme.
    Démarre une nouvelle partie de Démineur.
    """
    game = Minesweeper()
    game.play()
