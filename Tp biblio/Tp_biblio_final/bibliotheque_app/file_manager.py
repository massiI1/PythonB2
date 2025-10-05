import csv
import pickle
from .models import Bibliotheque, Livre, LivreNumerique
from .exceptions import ErreurBibliotheque, FichierIntrouvableErreur, FichierInvalideErreur

class BibliothequeAvecFichier(Bibliotheque):
    """Bibliothèque avec gestion de persistance (CSV / Pickle)."""

    def sauvegarder_csv(self, chemin_fichier: str):
        try:
            with open(chemin_fichier, mode='w', newline='', encoding='utf-8') as fichier:
                writer = csv.writer(fichier)
                writer.writerow(["Titre", "Auteur", "ISBN", "TailleFichier"])
                for livre in self.livres:
                    taille = getattr(livre, "taille_fichier", "")
                    writer.writerow([livre.titre, livre.auteur, livre.isbm, taille])
        except Exception as e:
            raise ErreurBibliotheque(f"Erreur lors de l’écriture du fichier CSV : {e}")
        else:
            print("Sauvegarde CSV réussie.")
        finally:
            print("sauvegarde CSV terminée.")

    def charger_csv(self, chemin_fichier: str):
        try:
            with open(chemin_fichier, mode='r', encoding='utf-8') as fichier:
                lecteur = csv.DictReader(fichier)
                for ligne in lecteur:
                    if ligne["TailleFichier"]:
                        livre = LivreNumerique(ligne["Titre"], ligne["Auteur"], ligne["ISBN"], float(ligne["TailleFichier"]))
                    else:
                        livre = Livre(ligne["Titre"], ligne["Auteur"], ligne["ISBN"])
                    self.ajouter_livre(livre)
        except FileNotFoundError:
            raise FichierIntrouvableErreur("Le fichier CSV est introuvable.")
        except Exception as e:
            raise FichierInvalideErreur(f"Erreur lors du chargement du CSV : {e}")
        else:
            print("✅ Chargement CSV réussi.")
        finally:
            print("🔁 Opération de lecture CSV terminée.")

    def sauvegarder_pickle(self, chemin_fichier: str):
        try:
            with open(chemin_fichier, 'wb') as fichier:
                pickle.dump(self.livres, fichier)
        except Exception as e:
            raise ErreurBibliotheque(f"Erreur lors de la sauvegarde Pickle : {e}")
        else:
            print("✅ Sauvegarde Pickle réussie.")
        finally:
            print("🔁 Opération Pickle terminée.")

    def charger_pickle(self, chemin_fichier: str):
        try:
            with open(chemin_fichier, 'rb') as fichier:
                self.livres = pickle.load(fichier)
        except FileNotFoundError:
            raise FichierIntrouvableErreur("Le fichier Pickle est introuvable.")
        except Exception as e:
            raise FichierInvalideErreur(f"Erreur lors du chargement Pickle : {e}")
        else:
            print("✅ Chargement Pickle réussi.")
        finally:
            print("🔁 Opération de lecture Pickle terminée.")
