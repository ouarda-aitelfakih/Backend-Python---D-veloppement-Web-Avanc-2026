class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("L'âge doit être un entier")
        if valeur < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        if valeur > 150:
            raise ValueError("L'âge semble irréaliste")
        self._age = valeur

personne1 = Personne("Ouarda", 20)
print(f"Âge initial : {personne1.age}")   # 20

personne1.age = 30
print(f"Nouvel âge  : {personne1.age}")   # 30
