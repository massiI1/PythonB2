class Vehicule:
    def __init__(self, marque: str, modele: str):
        self.marque = marque
        self.modele = modele

    def afficher_infos(self):
        print(f"Véhicule : {self.marque} {self.modele}")



class Voiture(Vehicule):
    def __init__(self, marque: str, modele: str, nombre_porte: int):
        super().__init__(marque, modele)  
        self.nombre_porte = nombre_porte

    def afficher_infos(self):
        print(f"Voiture : {self.marque} {self.modele}, {self.nombre_porte} portes")



class Moto(Vehicule):
    def __init__(self, marque: str, modele: str, type_moteur: str):
        super().__init__(marque, modele)   
        self.type_moteur = type_moteur

    def afficher_infos(self):
        print(f"Moto : {self.marque} {self.modele}, moteur {self.type_moteur}")


vehicule = Voiture("Peugeot", "208", 5)


moto = Moto("Yamaha", "R1", "4 cylindres")


vehicule.afficher_infos()
moto.afficher_infos()
