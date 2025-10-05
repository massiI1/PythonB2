class ErreurBibliotheque(Exception):
    """Exception de base pour la bibliothèque."""
    pass

class FichierIntrouvableErreur(ErreurBibliotheque):
    """Levée quand un fichier est manquant ou illisible."""
    pass

class FichierInvalideErreur(ErreurBibliotheque):
    """Levée quand le contenu d’un fichier est invalide."""
    pass
