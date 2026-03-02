number=0

contacts=["Bouchra","Ahmed","Sara"]

while number!=3:
     # afficher le menu
     print("1. Ajouter un contact à une liste")
     print("2. Afficher tous les contacts avec une numérotation")
     print("3. Quitter le programme")

     try:
         number=int(input("entrez votre choix : " ))

        #choix 1 :ajouter
         if number==1:
              newContact=input("entrer un nouveau contact:")
              contacts.append(newContact)
              print("contact ajouté")
        
        #choix 2 :afficher
         elif number==2:
              print("=============================")
              for i, contact in enumerate(contacts,start=1):
                   
                   print(i,"/",contact)
                  
              print("===============================")  

        #choix 3 :quitter      
         elif number ==3:
              print("Au revoir")
        #autre nombre que 1 ,2 et 3 
         else:
              print("choix invalise , entrez 1 ,2 ou 3")
    #autre type que entier
     except ValueError:
          print("veuillez entrer un nombre.")


            
              
                   
              
