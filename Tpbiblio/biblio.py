class Livre:
    def __init__(self, titre: str, auteur: str, isbm: str):
        self.titre = titre
        self.auteur = auteur
        self.isbm = isbm

    def infos(self):
        return(f"{self.titre} ecrit par {self.auteur} ISBN : {self.isbm}")
    
class LivreNumerique(Livre):
    def __init__(self, titre, auteur, isbm, taille_fichier: float):
        super().__init__(titre, auteur, isbm)
        self.taille_fichier = taille_fichier

    def infos(self):
        return(f"{super().infos()}taille fichier : {self.taille_fichier}")

class Bibliotheque:
    def __init__(self, nom: str):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)

    def supprimer_livre(self, isbm: str):
        self.livres = [livre for livre in self.livres if livre.isbm != isbm]

    def recherche_par_titre(self, titre: str):
        resultats = [livre for livre in self.livres if livre.titre == titre]
        return resultats if resultats else None

    def recherche_par_auteur(self, auteur: str):
        resultats = [livre for livre in self.livres if livre.auteur == auteur]
        return resultats if resultats else None

    def afficher_livres(self):
        if not self.livres:
            return f"La bibliothèque '{self.nom}' est vide."
        return "\n".join([livre.infos() for livre in self.livres])


biblio = Bibliotheque("Médiathèque Centrale")

livre1 = Livre("1984", "George Orwell", "12345")
livre2 = LivreNumerique("Python 101", "J. Smith", "67890", 2.5)
livre3 = Livre("Animal Farm", "George Orwell", "54321")

biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.ajouter_livre(livre3)

print(biblio.afficher_livres())

print("\nRecherche par titre '1984':")
print([livre.infos() for livre in biblio.recherche_par_titre("1984")])

print("\nRecherche par auteur 'George Orwell':")
print([livre.infos() for livre in biblio.recherche_par_auteur("George Orwell")])


biblio.supprimer_livre("12345")
print("\nBiblio près suppression :")
print(biblio.afficher_livres())
