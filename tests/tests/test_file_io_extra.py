import io, os, pickle, csv, pytest
from src.file_manager import BibliothequeAvecFichier
from src.models import Livre, LivreNumerique
from src.exceptions import FichierInvalideErreur, FichierIntrouvableErreur

def test_charger_csv_malforme_declenche_invalide(tmp_path):
    # CSV avec en-têtes manquants -> KeyError -> FichierInvalideErreur
    bad_csv = tmp_path / "bad.csv"
    bad_csv.write_text("Col1,Col2\nA,B\n", encoding="utf-8")
    b = BibliothequeAvecFichier("bad")
    with pytest.raises(FichierInvalideErreur):
        b.charger_csv(str(bad_csv))

def test_charger_pickle_malforme_declenche_invalide(tmp_path):
    bad_pkl = tmp_path / "bad.pkl"
    bad_pkl.write_bytes(b"not a pickle")
    b = BibliothequeAvecFichier("badpkl")
    with pytest.raises(FichierInvalideErreur):
        b.charger_pickle(str(bad_pkl))

def test_sauvegarder_csv_et_pickle_basics(tmp_path):
    # couvre chemins "heureux" et exécution des blocs else/finally
    b = BibliothequeAvecFichier("ok")
    b.ajouter_livre(Livre("A","AA","111"))
    b.ajouter_livre(LivreNumerique("B","BB","222",2.0))
    csv_path = tmp_path / "out.csv"
    pkl_path = tmp_path / "out.pkl"

    b.sauvegarder_csv(str(csv_path))
    assert csv_path.exists()
    # relecture manuelle pour vérifier l'écrit
    rows = list(csv.reader(csv_path.open("r", encoding="utf-8")))
    assert rows[0] == ["Titre","Auteur","ISBN","TailleFichier"]
    assert len(rows) == 3

    b.sauvegarder_pickle(str(pkl_path))
    assert pkl_path.exists()

    b2 = BibliothequeAvecFichier("reload")
    b2.charger_pickle(str(pkl_path))
    assert len(b2) == 2

def test_erreurs_introuvable(tmp_path):
    b = BibliothequeAvecFichier("err")
    with pytest.raises(FichierIntrouvableErreur):
        b.charger_csv(str(tmp_path / "no.csv"))
    with pytest.raises(FichierIntrouvableErreur):
        b.charger_pickle(str(tmp_path / "no.pkl"))
