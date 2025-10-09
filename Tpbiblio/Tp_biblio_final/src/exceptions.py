class ErreurBibliotheque(Exception):
    """Exception personnalisée de base pour la bibliothèque."""
    def __init__(self, message: str, code_erreur: int = 0):
        super().__init__(message)
        self.code_erreur = code_erreur


class FichierIntrouvableErreur(ErreurBibliotheque):
    """Levée quand un fichier est manquant ou illisible."""
    pass


class FichierInvalideErreur(ErreurBibliotheque):
    """Levée quand le contenu d’un fichier est invalide."""
    pass
