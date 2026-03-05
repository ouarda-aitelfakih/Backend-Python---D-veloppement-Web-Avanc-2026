class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def AfficherInfos(self):
        print(f"Nom  : {self.nom}")
        print(f"Age  : {self.age}")


class Salarie(Personne):
    def __init__(self, nom, age, numeroSomme, salaire):
        Personne.__init__(self, nom, age)
        self.numeroSomme = numeroSomme
        self.salaire = salaire

    def AfficherInfos(self):
        Personne.AfficherInfos(self)
        print(f"Numéro Somme : {self.numeroSomme}")
        print(f"Salaire      : {self.salaire} MAD")

    def CalculerSalaire(self):
        salaire_net = self.salaire * 1.20
        print(f"Salaire net (bonus 20%) : {salaire_net} MAD")
        return salaire_net

class Etudiant(Personne):
    def __init__(self, nom, age, cneEtudiant, notes):
        Personne.__init__(self, nom, age)
        self.cneEtudiant = cneEtudiant
        self.notes = notes

    def AfficherInfos(self):
        Personne.AfficherInfos(self)
        print(f"CNE Etudiant : {self.cneEtudiant}")
        print(f"Notes        : {self.notes}")

    def CalculerMoyenne(self):
        moyenne = sum(self.notes) / len(self.notes)
        print(f"Moyenne : {moyenne:.2f}/20")
        return moyenne

class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, age, numeroSomme, salaire,
                 cneEtudiant, notes, departement, anneeInscription):
        # Initialisation des classes parentes
        Salarie.__init__(self, nom, age, numeroSomme, salaire)
        Etudiant.__init__(self, nom, age, cneEtudiant, notes)
        self.departement = departement
        self.anneeInscription = anneeInscription

    def AfficherInfos(self):
        print("===== Doctorant =====")
        print(f"Nom              : {self.nom}")
        print(f"Age              : {self.age}")
        print(f"Numéro Somme     : {self.numeroSomme}")
        print(f"Salaire          : {self.salaire} MAD")
        print(f"CNE Etudiant     : {self.cneEtudiant}")
        print(f"Notes            : {self.notes}")
        print(f"Département      : {self.departement}")
        print(f"Année Inscription: {self.anneeInscription}")
        print("=====================")


print("------ Test Salarié ------")
s = Salarie("Fatima Zahra", 35, "S-1023", 8000)
s.AfficherInfos()
s.CalculerSalaire()

print("\n------ Test Etudiant ------")
e = Etudiant("Yassine El Amrani", 22, "CNE-4567", [15, 17, 12, 18, 14])
e.AfficherInfos()
e.CalculerMoyenne()

print("\n------ Test Doctorant (Héritage Multiple) ------")
d = Doctorant(
        nom="Ouarda Ait El Fakih",
        age=27,
        numeroSomme="S-2001",
        salaire=6500,
        cneEtudiant="CNE-9999",
        notes=[18, 19, 17, 20],
        departement="Informatique",
        anneeInscription=2024
    )
d.AfficherInfos()
d.CalculerSalaire()
d.CalculerMoyenne()
