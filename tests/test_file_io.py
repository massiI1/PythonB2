import csv, os, pickle
from src.exceptions import FichierIntrouvableErreur, FichierInvalideErreur
from src.file_manager import BibliothequeAvecFichier
from src.models import Livre, LivreNumerique
import pytest

def test_sauvegarde_et_rechargement_csv(tmp_path):
    b = BibliothequeAvecFichier("CSV Médiathèque")
    b.ajouter_livre(Livre("1984","George Orwell","12345"))
    b.ajouter_livre(LivreNumerique("Python 101","J. Smith","67890",2.5))

    csv_path = tmp_path / "livres.csv"
    b.sauvegarder_csv(str(csv_path))

    assert csv_path.exists()
    with csv_path.open("r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert rows[0] == ["Titre","Auteur","ISBN","TailleFichier"]
    assert len(rows) == 3

    b2 = BibliothequeAvecFichier("Reload")
    b2.charger_csv(str(csv_path))
    assert len(b2) == 2
    assert [livre.titre for livre in b2.livres] == ["1984", "Python 101"]

def test_pickle_roundtrip(tmp_path):
    b = BibliothequeAvecFichier("Pickle Médiathèque")
    b.ajouter_livre(Livre("A","AA","1"))
    pkl_path = tmp_path / "livres.pkl"
    b.sauvegarder_pickle(str(pkl_path))
    assert pkl_path.exists()

    b2 = BibliothequeAvecFichier("ReloadPickle")
    b2.charger_pickle(str(pkl_path))
    assert len(b2) == 1
    assert b2.livres[0].titre == "A"

def test_erreurs_fichier(tmp_path):
    b = BibliothequeAvecFichier("Errors")
    with pytest.raises(FichierIntrouvableErreur):
        b.charger_csv(str(tmp_path / "nope.csv"))
    with pytest.raises(FichierIntrouvableErreur):
        b.charger_pickle(str(tmp_path / "nope.pkl"))
