motDePasse="python123"
match=0 #(le mot de passe est incorrect)

while match == 0:
    password=input("entrer le mot de passe : ")

    if password == motDePasse:
        match=1 #la boucle s'arrête , le mot de passe match 
        print("le mot de passe est correct !")
    else:
        print("Mot de passe incorrect, réessayez")
