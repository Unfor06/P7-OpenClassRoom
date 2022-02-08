import csv
import timeit

def glouton():

    actions = []

    with open('P7 OCR - Feuille 2(1).csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['price']= float (row['price'])
            row['profit']= float (row['profit'])
            row['dividende']= row['price']*row['profit']/100
            if row['price'] <= 0.01 or row['profit'] <= 0.01 :
                continue
            actions.append(list(row.values()))

    budget = 500
    panier = []
    action = None

    actions = sorted(actions, key=lambda a: float(a[3]), reverse=True)

    panier_action = []

    for action in actions:
        
        if action[1] <= budget:
            budget = budget - action[1]
            panier.append (float(action[3]))
            panier_action.append (action[0])
        else:
            continue

    print(panier_action)
    print(sum(panier))
print(timeit.timeit (glouton,number=1) )

