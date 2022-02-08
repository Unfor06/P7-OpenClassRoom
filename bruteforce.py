import itertools
import csv
import timeit


with open ("P7 OCR - Feuille 1.csv", "r") as l:
    l = csv.reader(l)
    
    actions = list(l)[1:]

def a ():

    meilleur_combinaison = None
    meilleur_rendemant = -1

    for panier_taille in range (1,len(actions)+1):
        print(F"{panier_taille}//20")

        for action_panier in itertools.combinations(actions, panier_taille):
            rendemant = 0
            cout = 0
            
            for action in action_panier:
                rendemant += float(action[-1].replace (",", "."))
                cout += float(action[1].replace(",", "."))
                
            if cout > 500:
                continue

            if rendemant > meilleur_rendemant:
                meilleur_combinaison = action_panier
                meilleur_rendemant = rendemant

        print(meilleur_combinaison)
        print(meilleur_rendemant)        

print(timeit.timeit(a, number=1))



