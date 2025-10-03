class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant: float):
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant} effectué. Nouveau solde : {self.solde}")
        else:
            print("Le montant du dépôt doit être positif.")

    def retirer(self, montant: float):
        if montant > self.solde:
            print(f"Vous ne posséder pas assez d'argent sur votre solde. Solde actuel : {self.solde}")
        else:
            self.solde -= montant
            print(f"Vous venez de retirer {montant}. Votre nouveau solde est de : {self.solde}")

    def afficher_solde(self):
        print(f"Le compte bancaire de {self.titulaire} possède actuellement {self.solde}")

compte = CompteBancaire("Maxime", 73783)
compte.retirer(30000)
compte.afficher_solde()

