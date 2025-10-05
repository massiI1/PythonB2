from .models import Livre, LivreNumerique
from .file_manager import BibliothequeAvecFichier

def main():
    biblio = BibliothequeAvecFichier("Médiathèque Centrale")

    livre1 = Livre("1984", "George Orwell", "12345")
    livre2 = LivreNumerique("Python 101", "J. Smith", "67890", 2.5)
    livre3 = Livre("Animal Farm", "George Orwell", "54321")

    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    biblio.ajouter_livre(livre3)

    print(biblio.afficher_livres())

   
    biblio.sauvegarder_csv("livres.csv")
    nouvelle_biblio = BibliothequeAvecFichier("Nouvelle Médiathèque")
    nouvelle_biblio.charger_csv("livres.csv")


   
    biblio.sauvegarder_pickle("livres.pkl")
    nouvelle_biblio.charger_pickle("livres.pkl")


if __name__ == "__main__":
    main()
