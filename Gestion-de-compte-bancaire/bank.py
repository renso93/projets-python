class Bank:
    def __init__(self, solde_initial: float = 0):
        self.solde = solde_initial

    def depot(self, montant:float)->str:
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self.solde += montant
        return f"Vous venez d'effectuer un dépôt de {montant} avec succès "

    def __str_(self):
        return f"Votre compte principal est de {self.solde}"

    def retrait(self, montant:float)->str:
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        
        if montant > self.solde:
            raise ValueError(f"Solde insuffisant")

        self.solde -= montant
        return f"Vous venez d'effectuer un retrait de {montant} avec succès "

    def __str__(self):
        return f"Votre compte principal est de {self.solde}"

    def get_solde(self):
        return self.solde
    
    def set_solde(self, solde: float):
        if solde < 0:
            raise ValueError("Le solde ne peut pas être négatif.")
        self.solde = solde

    def transfert(self, montant: float, compte_destinataire: 'Bank') -> str:
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        
        if montant > self.solde:
            raise ValueError("Solde insuffisant pour effectuer le transfert.")
        
        self.solde -= montant
        compte_destinataire.depot(montant)
        return f"Vous venez d'effectuer un transfert de {montant} vers le compte destinataire avec succès."

    def __str__(self):
        return f"Votre compte principal est de {self.solde}"

    def __repr__(self):
        return f"Bank(solde={self.solde})"

    def __eq__(self, other):
        if isinstance(other, Bank):
            return self.solde == other.solde
        return False
    
bank = Bank()
dp = bank.depot(4500000)
print(dp)
print(bank)
rt = bank.retrait(100000)
print(rt)
tr = bank.transfert(200000, Bank())
print(tr)
print(bank)