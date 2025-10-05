# TP Bibliothèque Python

## Présentation
Ce TP illustre la mise en place d'une application de gestion de bibliothèque en Python :
- Classes et héritage (Livre, LivreNumérique, Bibliothèque)
- Sérialisation/désérialisation (Pickle)
- Lecture et écriture de données tabulaires (CSV)
- Gestion d'exceptions personnalisées
- Structure modulaire avec packages et imports relatifs

## Structure des fichiers
```
bibliotheque_app/
    __init__.py          # Déclare le package
    models.py            # Définit les classes Livre, LivreNumérique et Bibliothèque
    file_manager.py      # BibliothèqueAvecFichier : gestion des CSV et Pickle
    exceptions.py        # Exceptions personnalisées (ErreurBibliotheque...)
    main.py              # Point d'entrée : instancie, teste et exécute l'app
```
Un fichier `tp_biblio_original.py` contient votre ancien code pour référence.

## Exécution
Depuis VS Code ou un terminal :
```
cd "Tp biblio"
python -m bibliotheque_app.main
```
Cela exécute le script principal qui :
- Ajoute des livres à la bibliothèque
- Sauvegarde en CSV et Pickle
- Recharge les données et les affiche

## Notions couvertes
- Modules et packages Python
- Imports relatifs
- Sérialisation avec Pickle
- Lecture/écriture CSV
- Gestion des exceptions (try/except/else/finally)
- Exceptions personnalisées (raise)
