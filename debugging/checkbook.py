#!/usr/bin/env python3
class CarnetDeCheques:
    """
    Représente un carnet de chèques simple.

    Attributs :
    ----------
    solde : float
        Le solde actuel du carnet de chèques.

    Méthodes :
    ----------
    deposer(montant)
        Ajoute un montant au solde.
    retirer(montant)
        Retire un montant du solde si les fonds sont suffisants.
    afficher_solde()
        Affiche le solde actuel.
    """

    def __init__(self):
        """Initialise un carnet de chèques avec un solde de 0."""
        self.solde = 0.0

    def deposer(self, montant):
        """
        Dépose un montant dans le carnet.

        Paramètres :
        -----------
        montant : float
            Montant à déposer (doit être positif).
        """
        self.solde += montant
        print("Vous avez déposé {:.2f} €".format(montant))
        print("Solde actuel : {:.2f} €".format(self.solde))

    def retirer(self, montant):
        """
        Retire un montant du carnet si le solde est suffisant.

        Paramètres :
        -----------
        montant : float
            Montant à retirer (doit être positif).
        """
        if montant > self.solde:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.solde -= montant
            print("Vous avez retiré {:.2f} €".format(montant))
            print("Solde actuel : {:.2f} €".format(self.solde))

    def afficher_solde(self):
        """Affiche le solde actuel du carnet de chèques."""
        print("Solde actuel : {:.2f} €".format(self.solde))


def saisir_montant_valide(message):
    """
    Demande à l'utilisateur de saisir un montant valide et positif.

    Paramètres :
    -----------
    message : str
        Le message à afficher à l'utilisateur pour la saisie.

    Retour :
    --------
    float
        Le montant saisi par l'utilisateur, toujours positif.
    """
    while True:
        try:
            montant = float(input(message))
            if montant <= 0:
                print("Veuillez entrer un montant positif.")
                continue
            return montant
        except ValueError:
            print("Entrée invalide. Veuillez saisir un nombre.")


def main():
    """
    Fonction principale du programme.

    Permet à l'utilisateur d'interagir avec le carnet de chèques
    via un menu pour déposer, retirer, afficher le solde ou quitter.
    """
    cb = CarnetDeCheques()
    while True:
        action = input("Que souhaitez-vous faire ? (deposer, retirer, solde, quitter) : ").lower()
        if action == 'quitter':
            print("Au revoir !")
            break
        elif action == 'deposer':
            montant = saisir_montant_valide("Entrez le montant à déposer : ")
            cb.deposer(montant)
        elif action == 'retirer':
            montant = saisir_montant_valide("Entrez le montant à retirer : ")
            cb.retirer(montant)
        elif action == 'solde':
            cb.afficher_solde()
        else:
            print("Commande invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
