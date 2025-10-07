from src.models import Bibliotheque, Livre, LivreNumerique
from src.exceptions import ErreurBibliotheque
import pytest

def test_creation_bibliotheque(bibliotheque_vide):
    assert bibliotheque_vide.nom == "Bibliothèque Test"
    assert len(bibliotheque_vide) == 0

def test_ajouter_livre(bibliotheque_vide, livre_python):
    ok = bibliotheque_vide.ajouter_livre(livre_python)
    assert ok is True
    assert len(bibliotheque_vide) == 1
    assert bibliotheque_vide.livres[0].titre == "Python"

def test_recherche_par_titre_et_auteur(bibliotheque_vide):
    b = bibliotheque_vide
    b.ajouter_livre(Livre("Python", "Alpha", "111"))
    b.ajouter_livre(Livre("Java", "Beta", "222"))
    b.ajouter_livre(LivreNumerique("Python", "Gamma", "333", 1.2))

    assert [l.titre for l in b.recherche_par_titre("Python")] == ["Python", "Python"]
    assert [l.auteur for l in b.recherche_par_auteur("Beta")] == ["Beta"]

def test_doublon_isbn_declenche_exception(bibliotheque_vide):
    b = bibliotheque_vide
    b.ajouter_livre(Livre("X", "A", "999"))
    with pytest.raises(ErreurBibliotheque) as exc:
        b.ajouter_livre(Livre("Y", "B", "999"))
    assert getattr(exc.value, "code_erreur", 0) == 1001
    assert "existant" in str(exc.value) or "existe" in str(exc.value)
