class Vehicule:
    def __init__(self, marque, vitesse):
        self.marque  = marque
        self.vitesse = vitesse
        print(f"Véhicule {marque} créé")

    def accelerer(self):
        print(f"{self.marque} accélère")

    def freiner(self):
        print(f"{self.marque} freine")

class Voiture(Vehicule):
    def __init__(self, marque, vitesse, nb_portes):
        super().__init__(marque, vitesse)   # Appelle le constructeur parent
        self.nb_portes = nb_portes
        print(f"Voiture avec {nb_portes} portes")

ma_voiture = Voiture("Peugeot", 0, 5)
print()
ma_voiture.accelerer()    # Méthode héritée
ma_voiture.freiner()      # Méthode héritée

print(f"Nombre de portes : {ma_voiture.nb_portes}")
