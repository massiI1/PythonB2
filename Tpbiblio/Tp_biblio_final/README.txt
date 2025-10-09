Bibliothèque Python — Gestion de livres (CSV / Pickle)

Ce dépôt contient un mini-projet de gestion de bibliothèque (livres papier et numériques), avec persistance **CSV** et **Pickle**, une API objet simple et une suite de tests **pytest**.

## Fonctionnalités
- Gestion de livres (papier & numériques) via `src.models` (classes `Livre`, `LivreNumerique`, `Bibliotheque`).
- Persistance CSV & Pickle via `src.file_manager.BibliothequeAvecFichier` (méthodes `sauvegarder_csv`, `charger_csv`, `sauvegarder_pickle`, `charger_pickle`).
- Exceptions dédiées dans `src.exceptions` (`ErreurBibliotheque`, `FichierIntrouvableErreur`, `FichierInvalideErreur`).
- Tests `pytest` configurés via `pyproject.toml` avec fixtures dans `tests/conftest.py`.

## 🗂️ Arborescence (principale)

```
nouveau_PythonB2_updated/
  nouveau_PythonB2_updated/

```

>  D’autres dossiers d’exercices sont présents (`exercices 1`, `exercices 2`, etc.) mais la logique principale exploitable se trouve dans **`Tp biblio\Tp_biblio_final\src`** et les tests dans **`tests/`**.

##  Prise en main

### 1 Créer et activer un environnement virtuel
**Windows (cmd):**
```bat
cd nouveau_PythonB2_updated\nouveau_PythonB2_updated
python -m venv .venv
.\.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
cd nouveau_PythonB2_updated/ nouveau_PythonB2_updated
python3 -m venv .venv
source .venv/bin/activate
```

### 2 Installer les dépendances
Si le fichier `requirements.txt` est présent à la racine interne:
```bash
pip install -r requirements.txt
```
Sinon, installez à minima :
```bash
pip install pytest pandas==2.3.3 flask
```

### 3 Lancer les tests
```bash
pytest -q
```
Si votre shell ne se trouve pas dans le dossier qui contient `tests/`, ciblez-le explicitement :
```bash
pytest -q tests
```

### 4 Couverture de code (facultatif)
```bash
pip install pytest-cov
pytest tests --cov="Tp biblio\Tp_biblio_final\src" --cov-report=term-missing
# Rapport HTML :
pytest tests --cov="Tp biblio\Tp_biblio_final\src" --cov-report=html
# Puis ouvrez htmlcov/index.html
```

## 🧩 API — Classes principales

### `src.models`
- **`Livre(titre: str, auteur: str, isbm: str)`**  
  Représente un livre.  
  - `infos() -> str`: retourne une chaîne lisible `"Titre écrit par Auteur ISBN : isbm"`.

- **`LivreNumerique(Livre)`**  
  Ajoute l’attribut `taille_fichier: float`.

- **`Bibliotheque(nom: str)`**  
  - `ajouter_livre(livre) -> bool`: ajoute un livre (l’**ISBN** doit être unique). En cas de doublon, lève `ErreurBibliotheque` avec `code_erreur=1001`.
  - `supprimer_livre(isbm: str) -> None`: supprime par ISBN (silencieux si l’ISBN n’existe pas).
  - `__len__() -> int`: nombre de livres.
  - `recherche_par_titre(titre: str) -> list[Livre]`
  - `recherche_par_auteur(auteur: str) -> list[Livre]`
  - `afficher_livres() -> str`: affiche l’état de la bibliothèque (message dédié si vide).

>  **Note:** le champ est nommé `isbm` dans le code (et non `isbn`). Les tests et la persistance utilisent la même orthographe.

### `src.file_manager`
- **`BibliothequeAvecFichier(Bibliotheque)`**  
  - `sauvegarder_csv(chemin_fichier: str)` : écrit les colonnes `Titre, Auteur, ISBN, TailleFichier`.
  - `charger_csv(chemin_fichier: str)` : recharge les livres à partir d’un CSV ; lève `FichierIntrouvableErreur` si le fichier n’existe pas et `FichierInvalideErreur` si le contenu est incorrect.
  - `sauvegarder_pickle(chemin_fichier: str)` / `charger_pickle(chemin_fichier: str)` : sérialisation/chargement via `pickle` avec la même gestion d’erreurs.

### `src.exceptions`
- `ErreurBibliotheque(message: str, code_erreur: int = 0)`
- `FichierIntrouvableErreur(ErreurBibliotheque)`
- `FichierInvalideErreur(ErreurBibliotheque)`

##  Exécuter la démo (script principal)

Un script de démonstration est fourni :
```bash
python "Tp biblio\Tp_biblio_final\src\main.py"
```
Il instancie une bibliothèque, ajoute des livres, illustre les recherches et la persistance.

##  Tests & organisation

- Les tests vivent dans **`tests/`** et `pyproject.toml` configure `pytest` (patterns des fichiers/ fonctions de test).
- `tests/conftest.py` prépare le `PYTHONPATH` pour que les imports `from src...` fonctionnent.
- Pour n’exécuter qu’un seul test/fichier :
  ```bash
  pytest -q tests/test_models.py
  pytest -q tests/test_file_io.py::test_sauvegarde_et_rechargement_csv
  ```
