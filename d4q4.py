#Nom: Mohamed Ismail Asaklil
#Numero d'etudiant: 0300243534

#QUESTION 4



###################################################################################################################################





# Jeu de cartes.

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

#ces premieres fonctions sont deja completees pour vous, ne les changez pas

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'a ce que l'usager appuie Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente toutes les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)
    
#######################################################################################
#Les fonctions precedentes sont deja completees
#Completez les fonctions apres ce commentaire
#######################################################################################
    
def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]


     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     
     for i in range(0,len(p)):
         if i%2==0: #VU QUE C EST LE ROBOT QUI DISTRIBUE DONC IL DONNE LA PREMIER CARTE A HUMAIN ET INDEX DE LA PREMIERE CARTE EST 0 DONC PAIRE
#TANDIS QUE CELLE QUI VA DONNER A LUI MEME SON INDEX EST 1 DONC IMPAIRE
             autre.append(p[i])
         else:
             donneur.append(p[i]) #faire integrer des elements a la liste de cartes       
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copie de la liste l avec toutes les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]
    l.sort()

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    resultat = l 
    compteur= 0 #il faut faire un compteur car si on elimine un doublon et qu il y a un autre doublon qui le suit
    #il faut que l'index s initialise cad vu que les premiers doublons d index 0 et 1 sont supp il faut que ceux qui les suivent
    #aient le meme index cad PRENDRE LEURS POSITIONS
    for i in range(len(resultat) + compteur):
        if i < (len(resultat)+ compteur - 1 ):
            if resultat[i - compteur][0] == resultat[i+1 - compteur][0]: #J AI AJOUTE LE COMPTEUR CAR SI PAR EXEMPLE DEUX ELEMENTS S'ENLEVENT DONC L'INDEX DE CEUX QUI LES SUIVENT VA PRENDRE LA POSITION DE CEUX SUPPRIMES
                resultat = resultat[0:i - compteur] + resultat[i+2 - compteur:]#pour enregistrer seulement des le debut de la liste vers le premier doublon(exclus) puis du deuxieme doublon (exclus) jusqu'a len()-1
                compteur += 1 #INCREMENTER LE COMPTEUR A L INTR DE IF
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None 
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    resultat="" #str vide
    for i in range(0,len(p)):
        resultat=resultat+" "+p[i] #des str separes par espaces
        if i==len(p)-1:
            print(resultat)#afficher le resultat
        
    

    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier lu au clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas entre 1 et n
     
     Précondition: n>=1
     '''
    

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     n>=1
     x=int(input("SVP entrer un entier de "+str(1)+" à "+str(n)+" : "))
     if x>=1 and x<=n: #le if avant la boucle pour valider le cas ou le joueur entre un nb entre 1 et n des la premiere tentaive
         print("Vous avez demande ma "+str(x)+"ème carte.") 
     else:
         while x<1 or x>n: #le while a la place du for car on ne sait pas le nb de boucle
             x=int(input("SVP entrer encore une fois un entier de "+str(1)+" à "+str(n)+" : "))
             if x>=1 and x<=n:
                 print("Vous avez demande ma "+str(x)+"ème carte.")
             
         
     
     
     
     

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     i=0
     while i>=0: #on utilise le while car on ne sait pas en cm de tour la partie de carte va se finir
    #le nb de boucle indefini ==> l'utilisation de WHILE
         if i%2==0: #on constate que c est tjrs l'Humain qui commence a jouer car c est ROBOT qui a distribué les cartes
             print("Votre tour")
             print("Votre main est:")
             affiche_cartes(humain)
             print("J'ai "+str(len(donneur))+" cartes. Si 1 est la position de ma première carte et "+str(len(donneur))+" est la position de ma dernière carte, laquelle de mes cartes vous voulez?") 
             entrez_position_valide(len(donneur))
             x=donneur[random.randint(1,len(donneur)-1)]#j'utilise la fct random pour l'index pour que ca me donne une carte au hasard de Robot.
             donneur.remove(x) #vu que l Humain va prendre la carte donc elle n'appartiendra plus a la liste de Robot
             #il faut la supprimer par consequent
             print("La voilà. C'est un ",x)
             print("Avec "+str(x)+" ajouté, votre main est:")
             humain.append(x) #pour ajouter la carte prise de chez Robot dans la liste des cartes de Humain
             affiche_cartes(humain) 
             #DEFAUSSER LES PAIRES ET MELANGER LES CARTES DE CETTE LISTE
             print("Après défaussé toutes les paires et mélanger les cartes, votre main est:")
             humain=elimine_paires(humain)
             affiche_cartes(humain)
             attend_le_joueur()
             i+=1 ####### Il ne faut pas oublier d'incrementer le compteur pour que le tour soit au prochain
######NE PAS L INCREMENTER A L EXT DU IF STATEMENT CAR SINN ON NE POURRA PAS AVOIR UNE CONTRE CONDITION POUR STOPPER LA BOUCLE
             
         else:
             print("Mon tour.")
             Y=random.randint(1,len(humain)-1)#je note la variable Y qui est un random de la derniere liste a la fin du 1er tour
             print("J'ai pris votre "+str(Y)+"ème carte.") #on a utilise le random pour choisir au hasard
             #IL NE FAUT PAS OUBLIER QUE CA DOIT CHOISIR UN NB AU HASARD PAR RAPPORT A LEN() DE LA LISTE REDUITE CAD APRES AVOIR SEPARER LES PAIRES DEUX FOIS
             donneur.append(humain[Y-1])#car le Robot a pris une de mes cartes
             humain.remove(humain[Y-1]) #vu que le Robot va prendre ma carte du coup je dois la supp de mes cartes
             donneur=elimine_paires(donneur) 
             attend_le_joueur()
             i+=1 ####### Il ne faut pas oublier d'incrementer le compteur pour que le tour soit au prochain
######NE PAS L INCREMENTER A L EXT DU IF STATEMENT CAR SINN ON NE POURRA PAS AVOIR UNE CONTRE CONDITION POUR STOPPER LA BOUCLE            

         if len(donneur)==1 and len(humain)!=1: #DANS LE CAS OU LA LISTE DE CARTE DE ROBOT CONTIENT 1 CARTE DONC C EST ROBOT QUI A GAGNE
             print("J'ai terminé toutes les cartes.")
             print("Vous avez perdu! Moi, Robot, j'ai gagné.")
             i=-1 #pour arreter la boucle il faut donner une contre condition car on a pas le droit au break
         if len(humain)==1 and len(donneur)!=1:#DANS LE CAS OU LA LISTE DE CARTE DE HUMAIN CONTIENT 1 CARTE DONC C EST HUMAIN QUI A GAGNE
             print("J'ai terminé toutes les cartes.")
             print("Felicitations! Vous, Humain, vous avez gagné.")
             i=-1 #pour arreter la boucle il faut donner une contre condition car on a pas le droit au break
          
             
        
         

     
     
     
     
     
     
    

	 
# programme principale deja completé
joue()


##################################################################################################################
'''
Un exemple de partie gagnee par Humain:
---------------------------------------

Bonjour. Je m'appelle Robot et je distribue les cartes.
Votre main est:
7♡ 4♠ 9♣ 5♣ 9♠ Q♡ A♠ 10♢ J♠ 5♡ 7♢ 6♢ 10♠ Q♢ 4♡ Q♣ J♡ 7♠ 6♡ 6♠ 3♠ 3♢ 8♠ 10♣ K♢ 6♣ 
Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.
Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
A♠ 7♢ Q♣ K♢ 10♣ 8♠ 
J'ai 7 cartes. Si 1 est la position de ma première carte et
7 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 7: 6
Vous avez demande ma 6ème carte.
La voila. C'est un A♣
Avec A♣ ajouté, votre main est:
A♠ 7♢ Q♣ K♢ 10♣ 8♠ A♣ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
8♠ Q♣ 10♣ 7♢ K♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2ème carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
8♠ 10♣ 7♢ K♢ 
J'ai 5 cartes. Si 1 est la position de ma première carte et
5 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 5: 3
Vous avez demande ma 3ème carte.
La voila. C'est un 10♡
Avec 10♡ ajouté, votre main est:
8♠ 10♣ 7♢ K♢ 10♡ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
7♢ 8♠ K♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 1ère carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
8♠ K♢ 
J'ai 3 cartes. Si 1 est la position de ma première carte et
3 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 3: 1
Vous avez demande ma 1ère carte.
La voila. C'est un K♣
Avec K♣ ajouté, votre main est:
8♠ K♢ K♣ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
8♠ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 1ère carte.
Appuyez Enter pour continuer. 
***********************************************************
J'ai terminé toutes les cartes.
Felicitations! Vous, Humain, vous avez gagné.
>>> 
'''

##################################################################################################################
'''
Un exemple de partie gagnee par Robot:
---------------------------------------

Bonjour. Je m'appele Robot et je donne les cartes.
Votre main de cartes est:
3♣ 6♣ 2♢ 10♡ 10♠ 8♢ 5♣ Q♣ 4♡ 8♠ 5♠ J♢ 3♢ A♠ 7♡ 3♠ A♣ 9♡ 3♡ 9♣ 8♣ 6♠ 7♣ 6♢ K♠ Q♠ 
Ne vous inquitez pas, je ne peux pas voir votres cartes ou leur ordre.
Maintenant defaussez toutes les paires de votre main. Je vais faire ca aussi.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
4♡ 2♢ J♢ 6♣ 8♣ K♠ 
J'ai 5 cartes. Si 1 est la position de ma premiere carte et
5 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 5: 5
Vous avez demande ma 5-eme carte.
La voila. C'est un K♣
Avec K♣ ajoute, votre main est:
4♡ 2♢ J♢ 6♣ 8♣ K♠ K♣ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
J♢ 6♣ 8♣ 4♡ 2♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2-eme carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
J♢ 8♣ 4♡ 2♢ 
J'ai 3 cartes. Si 1 est la position de ma premiere carte et
3 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 3: 3
Vous avez demande ma 3-eme carte.
La voila. C'est un 8♡
Avec 8♡ ajoute, votre main est:
J♢ 8♣ 4♡ 2♢ 8♡ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
4♡ 2♢ J♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2-eme carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
4♡ J♢ 
J'ai 1 cartes. Si 1 est la position de ma premiere carte et
1 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 1: 1
Vous avez demande ma 1-ere carte.
La voila. C'est un 4♣
Avec 4♣ ajoute, votre main est:
4♡ J♢ 4♣ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
J♢ 
Appuyez Enter pour continuer. 
J'ai terminé toutes les cartes.
Vous avez perdu! Moi, Robot, j'ai gagné.
>>> 
'''
##################################################################################################################
