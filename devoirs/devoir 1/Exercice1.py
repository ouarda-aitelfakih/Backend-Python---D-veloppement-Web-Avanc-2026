#convertir en entier dans une ligne ( input et int )
age=int(input("entrez votre age: "))

#utiliser les conditions (if/elif/else)
if age>=0 and age<=12:
    print("vous êtes enfant")
elif age>=13 and age<=17:
    print("vous êtes adolescent")
elif age>=18 and age <64:
    print("vous êtes adult")
else :
    print("vous êtes senior")