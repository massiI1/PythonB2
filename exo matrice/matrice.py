etudiants = [
    {"nom" : "Alice", "note": 15, "annee": 2},
    {"nom": "Bob", "note": 12, "annee": 1},
    {"nom": "Charlie", "note": 18, "annee": 2}
]


etudiants_admis = [etudiant for etudiant in etudiants if etudiant["note"] >= 12]

notes_par_annee = {}
for etudiant in etudiants_admis:
    annee = etudiant["annee"]
    note = etudiant["note"]
    if annee not in notes_par_annee:
        notes_par_annee[annee] = []
    notes_par_annee[annee].append(note)

moyennes_par_annee = {
    annee: sum(liste_notes) / len(liste_notes)
    for annee, liste_notes in notes_par_annee.items()
}

def calculer_mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 15:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    else:
        return "Ajourné"

mentions_etudiants = {
    etudiant["nom"]: calculer_mention(etudiant["note"])
    for etudiant in etudiants_admis
}

print("Étudiants admis :", etudiants_admis)
print("Moyennes par année :", moyennes_par_annee)
print("Mentions :", mentions_etudiants)
