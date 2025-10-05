Ce TP consiste à développer une petite application Python qui permet de gérer une bibliothèque. L’objectif est d’apprendre de manière concrète plusieurs notions du cours : la programmation orientée objet avec des classes et de l’héritage (Livre, LivreNumérique, Bibliothèque), la sauvegarde et la restauration des données avec Pickle, la lecture et l’écriture de fichiers CSV pour manipuler des données tabulaires, la gestion des exceptions en Python (y compris la création de ses propres exceptions), et l’organisation d’un projet en modules et packages avec des imports relatifs.

Le code est organisé dans un package Python appelé bibliotheque_app. On y trouve les fichiers suivants :
– init.py qui marque le dossier comme package Python
– models.py qui définit les classes Livre, LivreNumérique et Bibliothèque
– file_manager.py qui gère la lecture et l’écriture des données en CSV et Pickle
– exceptions.py qui contient les exceptions personnalisées comme ErreurBibliotheque
– main.py qui est le point d’entrée de l’application, pour créer et tester la bibliothèque

Le script principal crée une bibliothèque, ajoute des livres papier et numériques, sauvegarde les données en CSV et Pickle, puis recharge les fichiers et affiche le contenu à l’écran.

Ce projet permet de mettre en pratique :
– L’organisation d’un projet Python en modules et packages
– L’utilisation des imports relatifs
– La sérialisation et désérialisation d’objets avec Pickle
– La lecture et l’écriture de données tabulaires avec CSV
– La gestion d’exceptions avec try/except/else/finally
– La création et l’utilisation d’exceptions personnalisées avec raise