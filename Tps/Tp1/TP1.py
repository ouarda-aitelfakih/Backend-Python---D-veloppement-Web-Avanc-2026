#======================================================================================================================
#                                                       TP1
#======================================================================================================================

donnees = [
("Sara", "Math", 12, "G1"),
("Sara", "Info", 14, "G1"),
("Ahmed", "Math", 9, "G2"),
("Adam", "Chimie", 18, "G1"),
("Sara", "Math", 11, "G1"),
("Bouchra", "Info", "abc", "G2"),
("", "Math", 10, "G1"),
("Yassine", "Info", 22, "G2"),
("Ahmed", "Info", 13, "G2"),
("Adam", "Math", None, "G1"),
("Sara", "Chimie", 16, "G1"),
("Adam", "Info", 7, "G1"),
("Ahmed", "Math", 9, "G2"),
("Hana", "Physique", 15, "G3"),
("Hana", "Math", 8, "G3"),
]



#=================================================================================================================
#                                                     Partie 1
#=================================================================================================================




def valider (enregistrement):
    nom , matiere , note , groupe =enregistrement
    
    if nom == "":
        return (False,"nom vide")
    
    if matiere == "":
        return(False,"matière vide")
    
    if groupe == "":
        return (False,"groupe vide")
    
    if not isinstance(note,(int,float)):
        return (False,"note non numérique")
    
    if note<0 or note >20:
        return (False,"note hors limite")
    
    return (True,"")

valides=[]
erreurs=[]
doublons_exact=set()

for enregistrement in donnees:
    resultat,raison=valider(enregistrement)
    if resultat:
        valides.append((enregistrement[0],enregistrement[1],float(enregistrement[2]),enregistrement[3]))
    else:
        erreurs.append({"ligne":enregistrement ,"raison":raison})


for enregistrement in donnees:
    if donnees.count(enregistrement)>1:
        doublons_exact.add(enregistrement)
    

print("Valides:", valides)
print("Erreurs:", erreurs)
print("Doublons:", doublons_exact)



#==================================================================================================================================
#                                                          Partie 2
#==================================================================================================================================




#pour regrouper toutes les matières sans aucun doublon on a choisir set()
matieres_distinctes=set()

for nom , matiere , note ,groupe in valides:
    matieres_distinctes.add(matiere)

#affichage
print("Matières distinctes :", matieres_distinctes)




note_par_etudiant={}

for nom , matiere , note , groupe in valides:
    if nom not in note_par_etudiant:
        note_par_etudiant[nom]={}            #on a creer un  sous dict pour la liste des notes pour chaque matiere
    if matiere not in note_par_etudiant[nom]:
        note_par_etudiant[nom][matiere]=[]
    
    note_par_etudiant[nom][matiere].append(note)

    print("\nNotes par étudiant :")
    for etudiant, matieres in note_par_etudiant.items():
        print(f"  {etudiant} : {matieres}")


etudiant_par_groupe={}                

for nom,matiere,note,groupe in valides:
    if groupe not in etudiant_par_groupe:
        etudiant_par_groupe[groupe]=set()     #utiliser set pour éviter les répétitions inutiles   
    
    etudiant_par_groupe[groupe].add(nom)


print("\nÉtudiants par groupe :")
for groupe, etudiant in etudiant_par_groupe.items():
    print(f"  {groupe} : {etudiant}")



#======================================================================================================================================
#                                                            Partie 3
#======================================================================================================================================




#fonction récursive pour la somme 
def calcule_somme(liste,index=0):
    if index == len(liste):
        return 0
    
    return liste[index]+calcule_somme(liste,index+1)

#fonction pour calculer la moyenne
def calcule_moyenne(liste):
    if len(liste)==0:
        return 0
    return calcule_somme(liste)/len(liste)

#moyenne par matiere pour chaque étudiant
moyenne_par_matiere={}

for etudiant,matieres in note_par_etudiant.items():
    moyenne_par_matiere[etudiant]={}
    for matiere,notes in matieres.items():
        moyenne_par_matiere[etudiant][matiere]=calcule_moyenne(notes)


print("Moyennes par matière :")
for etudiant, matieres in moyenne_par_matiere.items():
    print(f"  {etudiant} : {matieres}")

#moyenne générale par étudiant
moyenne_generale={}

for etudiant,matieres in note_par_etudiant.items():
    notes_generale=[]
    for notes in matieres.values():
        notes_generale+=notes
    moyenne_generale[etudiant]=calcule_moyenne(notes_generale)

print("\nMoyennes générales :")
for etudiant, moy in moyenne_generale.items():
    print(f"  {etudiant} : {moy:.2f}")    




#========================================================================================================================================
#                                                               Partie 4
#========================================================================================================================================




SEUIL_GROUPE_FAIBLE=10.0 #seuil configurable
SEUIL_ECART=8.0 #ecart min/max considéré comme inquétant

#regroupement des alertes détectées lors de l’analyse

alertes ={
    "notes_multiples": [], #anomalie1
    "profil_incomplet":[], #anomalie2
    "groupe_faible":[], #anomalie3
    "ecart_important":[] #anomalie4
    }

#anomalie 1 :étudiant avec plusieurs notes dans une même matière

for etudiant,matieres in note_par_etudiant.items():
    for matiere,notes in matieres.items():
        if len(notes)>1:
            alertes["notes_multiples"].append({
                "etudiant": etudiant,
                "matiere": matiere,
                "notes": notes
            })

#anomalie 2 : profil incomplet

for etudiant,matieres in note_par_etudiant.items():
    matieres_etudiant=set(matieres.keys())
    matieres_manquantes=matieres_distinctes - matieres_etudiant
    if matieres_manquantes:
        alertes["profil_incomplet"].append({
            "etudiant":etudiant,
            "matieres_manquantes":matieres_manquantes
        })

#anomalie 3: groupe dont la moyenne générale est faible
for groupe,etudiants in etudiant_par_groupe.items():
    notes_groupe=[]
    for etudiant in etudiants:
        for notes in note_par_etudiant[etudiant].values():
            notes_groupe +=notes
    moyenne_groupe=calcule_moyenne(notes_groupe)
    if moyenne_groupe<SEUIL_GROUPE_FAIBLE:
        alertes["groupe_faible"].append({
            "groupe":groupe,
            "moyenne":moyenne_groupe
        })

# anamalie 4: écart important entre min et max

for etudiant ,matieres in note_par_etudiant.items():
    toutes_notes=[]
    for notes in matieres.values():
        toutes_notes+=notes
    if len(toutes_notes)>=2:
        ecart=max(toutes_notes)-min(toutes_notes)
        if ecart>=SEUIL_ECART:
            alertes["ecart_important"].append({
                "etudiant":etudiant,
                "min": min(toutes_notes),
                "max":max(toutes_notes),
                "ecart":ecart
            })

# ── Affichage des alertes ────────────────────────────────────
print("\n========== RAPPORT D'ANOMALIES ==========")

print("\n[1] Notes multiples pour une même matière :")
if alertes["notes_multiples"]:
    for a in alertes["notes_multiples"]:
        print(f"  {a['etudiant']} — {a['matiere']} : {a['notes']}")
else:
    print("  Aucune anomalie détectée.")

print("\n[2] Profils incomplets :")
if alertes["profil_incomplet"]:
    for a in alertes["profil_incomplet"]:
        print(f" {a['etudiant']} manque : {a['matieres_manquantes']}")
else:
    print("  Aucune anomalie détectée.")

print("\n[3] Groupes à moyenne faible (seuil =", SEUIL_GROUPE_FAIBLE, ") :")
if alertes["groupe_faible"]:
    for a in alertes["groupe_faible"]:
        print(f"  {a['groupe']} — moyenne : {a['moyenne']}")
else:
    print("  Aucune anomalie détectée.")

print("\n[4] Écarts importants min/max (seuil =", SEUIL_ECART, ") :")
if alertes["ecart_important"]:
    for a in alertes["ecart_important"]:
        print(f" {a['etudiant']} — min:{a['min']} max:{a['max']} écart:{a['ecart']}")
else:
    print("  Aucune anomalie détectée.")

