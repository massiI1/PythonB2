import pytest
from src.models import Bibliotheque, Livre, LivreNumerique
from src.exceptions import ErreurBibliotheque

def test_infos_et_len_affichage_vide():
    b = Bibliotheque("Ma Biblio")
    assert len(b) == 0
    assert "est vide" in b.afficher_livres()

def test_ajout_suppr_et_affichage():
    b = Bibliotheque("Biblio")
    l1 = Livre("Python", "Guido", "111")
    l2 = LivreNumerique("Data", "Pandas", "222", 3.14)
    assert b.ajouter_livre(l1) is True
    assert b.ajouter_livre(l2) is True
    # affichage non vide
    out = b.afficher_livres()
    assert "Python" in out and "Data" in out
    # suppression par ISBN
    b.supprimer_livre("111")
    assert len(b) == 1
    # suppression idempotente (ne casse pas si l'ISBN n'existe plus)
    b.supprimer_livre("111")
    assert len(b) == 1

def test_recherche_par_titre_et_auteur_multiples():
    b = Bibliotheque("B")
    b.ajouter_livre(Livre("Python", "A", "1"))
    b.ajouter_livre(LivreNumerique("Python", "B", "2", 1.0))
    b.ajouter_livre(Livre("C++", "A", "3"))
    assert [l.titre for l in b.recherche_par_titre("Python")] == ["Python", "Python"]
    assert [l.isbm for l in b.recherche_par_auteur("A")] == ["1", "3"]

def test_doublon_declenche_code_erreur():
    b = Bibliotheque("B")
    b.ajouter_livre(Livre("X", "Y", "999"))
    with pytest.raises(ErreurBibliotheque) as exc:
        b.ajouter_livre(Livre("Z", "W", "999"))
    assert getattr(exc.value, "code_erreur", 0) == 1001
