class Livre:
    def __init__(self, titre: str, auteur: str, isbm: str):
        self.titre = titre
        self.auteur = auteur
        self.isbm = isbm

    def infos(self):
        return f"{self.titre} écrit par {self.auteur} ISBN : {self.isbm}"


class LivreNumerique(Livre):
    def __init__(self, titre, auteur, isbm, taille_fichier: float):
        super().__init__(titre, auteur, isbm)
        self.taille_fichier = taille_fichier

    def infos(self):
        return f"{super().infos()} | Taille fichier : {self.taille_fichier} Mo"


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
