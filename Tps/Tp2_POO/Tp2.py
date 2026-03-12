#|================================================================================================================|
#|                                                                                                                |
#|                                                  TP2                                                           |
#|                                                                                                                |
#|================================================================================================================|


#=================================================================================================================
#                                                  Partie1
#=================================================================================================================

#une classe abstraite est une classe qui définit une structure commune entre plusieurs classes ,mais elle ne peut pas être instanciée
#les classes filles qui hérite doit fournir une implémentation concrète des méthodes abstraite dans la classe abstraite 

#la classe de base 
from abc import ABC, abstractmethod
class Boisson(ABC):

    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass

    
    #méthode addition
    def __add__(self,other):
        desc =self.description() + "+" +other.description()
        prix = self.cout() + other.cout()
    
        return f"{desc},{prix}$"
    
    #méthode d'affichage
    def afficher(self):
        print(f"Commande:{self.description()}")
        print(f"Prix : {self.cout()}")     

#=================================================================================================================
#                                                  Partie2
#=================================================================================================================


#créer des boissons concretes héritant de la classe abstraite Boisson

#class Cafe
class Cafe(Boisson):
    def cout(self):
        return 2.0
    
    def description(self):
        return "Café simple"

#class The
class The(Boisson):
    def cout(self):
        return 1.5
    
    def description(self):
        return "Thé"
    
# Il est obligatoire d'implémenter les méthodes dans les classe filles

boisson = Cafe()            #la classe fille peut être instanciée

print(boisson.description())
print(boisson.cout())



#=================================================================================================================
#                                                  Partie3
#=================================================================================================================


#une classe décorateur a pour objective de modifier le comportement des classes existante
class DecorateurBoisson(Boisson):

    def __init__(self,boisson):
        self._boisson = boisson

#ajout de lait
class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout()+0.5
    
    def description(self):
        return self._boisson.description()+",Lait"

#ajout de sucre
class Sucre(DecorateurBoisson):

    def cout(self):
        return self._boisson.cout() + 0.2
    
    def description(self):
        return self._boisson.description() + ",Sucre"

#exemple:
boisson1 = The()
boisson1 = Lait(boisson1)
boisson1 = Sucre(boisson1)

print(boisson1.description())
print(boisson1.cout())

#=================================================================================================================
#                                                  Partie4
#=================================================================================================================

#on fait la surcharge de l'opération + pour deux boissons
#voir la ligne 28
#exemple:
menu = boisson + boisson1
print(menu)


#=================================================================================================================
#                                                  Partie5
#=================================================================================================================

#data classes sont des classes qui contenat uniquement des données
from dataclasses import dataclass

@dataclass               #dataclass est une classe simple qui contient juste des données
class Client:
    nom: str
    numero: int 
    points_fidelite: int = 0 


#=================================================================================================================
#                                                  Partie6
#=================================================================================================================


#1.Ajouter un ingrédient supplémentaire
#ajout de Caramel
class Caramel(DecorateurBoisson):

    def cout(self):
        return self._boisson.cout() + 0.5
    
    def description(self):
        return self._boisson.description() + ",Caramel"
    
#2.Implémenter la combinaison de boissons avec +
#déjà fait dans la partie 4

#3.ajouter une méthode permettant d'afficher une commande complète
#voir la ligne 34
#exemple:
print(boisson1.afficher())


#=================================================================================================================
#                                                  Partie7
#=================================================================================================================

#1.création de la classe Commande
class Commande:
    #initialiser la classe avec un attribut client et une liste de boisson vide 
    def __init__(self,Client):
        self.Client = Client
        self.boissons = []
    
    #méthode pour ajouter plusieur boissons
    def ajouter_boisson(self,boisson):
        self.boissons.append(boisson)

    #méthode pour permettant de calculer le prix total de la commande
    def prix_total(self) :
        return sum(b.cout() for b in self.boissons)
    
    #afficher le contenu de la commande
    def afficher(self):
        print(f"Client:{self.Client.nom}")
        for b in self.boissons:
            print(f" {b.description()} : {b.cout()}")
        print(f"Total : {self.prix_total()}$")

#2.classes dérivées
class CommandeSurPlace(Commande):
    def afficher(self):
        print("===Commande Sur place====")
        super().afficher()

class CommandeEmporter(Commande):
    def afficher(self):
        print("====Commande à Emporter===")
        super().afficher()

#3.Programme de fidélité
class Fidelite:
    def ajouter_points(self,client,montant):
        points_gagnes = int(montant) #une point par dollard
        client.points+points_gagnes
        print(f"+{points_gagnes} points -> Total : {Client.points} pts")

#4.héritage multiple
class CommandeFidele(Commande,Fidelite):
    def valider(self):
        self.afficher()
        self.ajouter_points(self.Client,self.prix_total())

#5.test complet

#Créer un client 
Client = Client("ouarda",1,20)

#Créer des boissons
b1 = Cafe()
b1 = Lait(b1)
b1 = Sucre(b1)
b2 = The()
b2 = Caramel(b2)

#créer une commande fidèle
Commande = CommandeFidele(Client)
Commande.ajouter_boisson(b1)
Commande.ajouter_boisson(b2)

Commande.valider()


#=================================================================================================================
#                                                  Partie8
#=================================================================================================================

#voir le rapport 
