class Personne:
    def __init__(self,nom,age,email):
        self.nom=nom
        self.age=age
        self.email=email

#Création d'une instance
personne1= Personne('ouarda',20,'ouarda@gmail.com')

#lecture des attributs 
print(f"Nom: {personne1.nom}")
print(f"Age: {personne1.age}")
print(f"Email: {personne1.email}")

#modification des attributs

personne1.nom ='ouarda ait el fakih'
personne1.age +=1
personne1.email='ouardaaitelfakih@gmail.com'

#vérification des changements

print(f"Nouveau nom :{personne1.nom}")
print(f"Nouvel age :{personne1.age}")