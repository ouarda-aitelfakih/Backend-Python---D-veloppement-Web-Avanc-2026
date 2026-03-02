number1=int(input("entrez le 1er nombre : "))
number2=int(input("entrez le 2eme nombre: "))

choix =input("choisir l'opération convenable (+ - * /): ")

#utiliser les conditions if / elif et else 
if choix == "+":
    print(f"l'addition des deux nombres est : {number1 + number2}")
elif choix == "-":
    print(f"la soustraction est : {number1 - number2}")
elif choix == "*":
    print(f"la multiplication est : {number1 * number2}")
elif choix == "/":
    # Empêche la division par zéro
    if number2 == 0 :
        print("la devision par 0 est impossible ")
    else:
         print(f"la division est : {number1 / number2}")

else:
    print("entrer un choix convenable ")



