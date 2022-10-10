#DENNE VERSION HAR UDKOMMENTERET DIVERSE PRINTS, SÅ MAN BARE FÅR SUMMARY
from random import randint

#Spørger brugeren om hærstørrelser
print("Welcome to Risk Battle Simulator!")
print("===============================================")
A_troops_initial = int(input("How many troops are attacking? "))
D_troops_initial = int(input("How many troops are defending? "))
simulations = int(input("How many simulations do you want? "))
A_wins = 0
D_wins = 0
print()
print("Alright,", A_troops_initial, "on", D_troops_initial, ", let's get started!")
print("===============================================")

#Slaget simuleres 10 gange
for x in range(0, simulations):
    A_troops = A_troops_initial
    D_troops = D_troops_initial
    #print("===============================================")
    #print("SIMULATION", x+1)
    

    #Kampen fortsætter så længe der er tropper tilbage
    while A_troops > 0 and D_troops > 0:

        #Bestemmer antal terninger ud fra antal tropper for A og D
        if A_troops >= 3:
                A_dice = 3
        else:
            A_dice = A_troops

        if D_troops >= 2:
            D_dice = 2
        else:
            D_dice = D_troops

        #Kaster A's terninger
        A_roll = []
        for i in range(0, A_dice):
            A_roll.append(randint(1, 6))
        A_roll.sort()
        A_roll.reverse()
        #print("A rolls", A_roll)

        #Kaster D's terninger
        D_roll = []
        for i in range(0, D_dice):
            D_roll.append(randint(1, 6))
        D_roll.sort()
        D_roll.reverse()
        #print("D rolls", D_roll)

        #Sammenligner slag og trækker tropper fra taberen
        for i in range(0, min(A_dice, D_dice)):
            if A_roll[i] > D_roll[i]:
                #print("A's", A_roll[i], "beats D's", D_roll[i])
                D_troops -= 1
            else:
                #print("D's", D_roll[i], "beats A's", A_roll[i])
                A_troops -= 1
        #print("A has", A_troops, "left")
        #print("D has", D_troops, "left")
        #print("---------------------------------------")

    if A_troops > 0:
        A_wins += 1
        #print("Attack won! Now has", A_wins, "wins.")
    if D_troops > 0:
        D_wins += 1
        #print("Defense won! Now has", D_wins, "wins.")

print("===============================================")
A_winrate = int(A_wins / simulations * 100)
print("!!! SUMMARY !!!")
print("Attacking with", A_troops_initial, "against", D_troops_initial,
      "has a winrate of", A_winrate, "% for the attacker.")
print("A winrate", A_winrate, "%")
