class Bank:
    """Classe représentant un compte bancaire avec des fonctionnalités de dépôt, retrait et transfert."""
    def __init__(self, solde_initial: float = 0):
        self.solde = solde_initial

    def depot(self, montant:float)->str:
        """Effectue un dépôt sur le compte bancaire.
        montant: Le montant à déposer (doit être positif).
        Retourne un message de confirmation du dépôt."""
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self.solde += montant
        return f"Vous venez d'effectuer un dépôt de {montant} avec succès "

    def __str_(self):
        return f"Votre compte principal est de {self.solde}"

    def retrait(self, montant:float)->str:
        """Effectue un retrait sur le compte bancaire.
        montant: Le montant à retirer (doit être positif et inférieur ou égal au solde).
        Retourne un message de confirmation du retrait."""
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        
        if montant > self.solde:
            raise ValueError(f"Solde insuffisant")

        self.solde -= montant
        return f"Vous venez d'effectuer un retrait de {montant} avec succès "

    def __str__(self):
        return f"Votre compte principal est de {self.solde}"

    def get_solde(self):
        """Retourne le solde actuel du compte bancaire."""
        return f"Solde: {self.solde}"

    def transfert(self, montant: float, compte_destinataire: 'Bank') -> str:
        """Effectue un transfert d'argent vers un autre compte bancaire.
        montant: Le montant à transférer (doit être positif et inférieur ou égal au solde).
        compte_destinataire: Le compte bancaire destinataire du transfert.
        Retourne un message de confirmation du transfert."""
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        
        if montant > self.solde:
            raise ValueError("Solde insuffisant pour effectuer le transfert.")
        
        self.solde -= montant
        compte_destinataire.depot(montant)
        return f"Vous venez d'effectuer un transfert de {montant} vers le compte destinataire avec succès."

    def __str__(self):
        return f"Votre compte principal est de {self.solde}"


def main():
    # Exemple d'utilisation de la classe Bank
    print(f"*" *40)
    compte1 = Bank(1000)    
    compte2 = Bank(500)

    print(f"*" *40)
    print(compte1.depot(200))  # Dépôt de 200 sur le compte1
    print(f"*" *40)
    print(compte1.retrait(150))  # Retrait de 150 du compte1
    print(f"*" *40)
    print(compte1.transfert(300, compte2))  # Transfert de 300 du compte1 vers le  compte2
    print(compte1)  # Affiche le solde du compte1

    print(f"*" *40)
    compte2 = Bank(500)
    print(compte2)  # Affiche le solde du compte2
    print(compte1.get_solde())  # Affiche le solde du compte1
    print(compte2.get_solde())  # Affiche le solde du compte2

if __name__ == "__main__":
    main()

