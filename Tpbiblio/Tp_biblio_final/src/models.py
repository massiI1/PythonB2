from .exceptions import ErreurBibliotheque
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
        """Initialise une bibliothèque vide."""
        self.nom = nom
        self.livres = []

    def __len__(self):
        return len(self.livres)

    def ajouter_livre(self, livre):
        if any(existing.isbm == getattr(livre, 'isbm', None) for existing in self.livres):
            raise ErreurBibliotheque("ISBN déjà existant", code_erreur=1001)
        self.livres.append(livre)
        return True

    def supprimer_livre(self, isbm: str):
        self.livres = [livre for livre in self.livres if livre.isbm != isbm]

    def recherche_par_titre(self, titre: str):
        resultats = [livre for livre in self.livres if livre.titre == titre]
        return resultats

    def recherche_par_auteur(self, auteur: str):
        resultats = [livre for livre in self.livres if livre.auteur == auteur]
        return resultats

    def afficher_livres(self):
        if not self.livres:
            return f"La bibliothèque '{self.nom}' est vide."
        return "\n".join([livre.infos() for livre in self.livres])
