#!/usr/bin/python3
import random


print("*****************\n")
print("Le joueur 1 commence !\n")
print("****************\n")

suite = True;
result1 = 0
while suite == True :
    temp = result1
    temp = result1 + random.randint(1,6)    
    if temp >= 9 :
        suite = False
        print("Vous avez perdu !")
    else :
        result1 = temp
        print("Résultats du tirage : ")
        print(result1)
        avis = input("Voulez-vous continuer ? (y/n)\n")
        if avis == "y" or avis == "yes" :
            suite = True
        elif avis == "n" or avis == "no" :
            suite = False
        else : 
            print("Nous n'avons pas compris votre choix ! Nous supposons que vous voulez arrêter ! \n")
            suite = False
print("****************\n")
    


print("****************\n")
print("Au joueur 2  !\n")
print("****************\n")

suite = True;
result2 = 0
while suite == True :
    
    temp = result2
    temp = result2 + random.randint(1,6)    
    if temp >= 9 :
        suite = False
        print("Vous avez perdu !")
    else :
        result2 = temp
        print("Résultats du tirage : ")
        print(result2)
        avis = input("Voulez-vous continuer ? (y/n)\n")
        if avis == "y" or avis == "yes" :
            suite = True
        elif avis == "n" or avis == "no" :
            suite = False
        else : 
            print("Nous n'avons pas compris votre choix ! Nous supposons que vous voulez arrêter ! \n")
            suite = False
# print("*****************\n")


if result1 > result2 :
    print("Le joueur 1 gagne !")
elif result1 < result2 :
    print("Le joueur 2 gagne !")
else :
    print("Egalité !")
