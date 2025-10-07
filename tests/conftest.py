# Ensure the library src path is importable
import sys
from pathlib import Path

PKG_ROOT = Path(__file__).resolve().parents[1] / "Tp biblio" / "Tp_biblio_final"
SRC_PATH = PKG_ROOT
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

import pytest
from src.models import Bibliotheque, Livre

@pytest.fixture
def bibliotheque_vide():
    """Fixture pour une bibliothèque vide."""
    return Bibliotheque("Bibliothèque Test")

@pytest.fixture
def livre_python():
    """Fixture pour un livre 'Python'."""
    return Livre("Python", "A. Developer", "123-456")
