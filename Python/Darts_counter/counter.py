from checkout_checker import checkout_recommendation
from points_counter import points_counter

rules = input("Do you want to see the rules / shortcuts for this program? (y/n): ")

print(" ") #tehdään tyhjä rivi ennen mahdollisia ohjeita

if rules == "y" or rules == "Y" or rules == "yes" or rules == "Yes":
    print("shortcuts and key binding for enter you darts score (0 if you miss) (press enter to skip throw) (d front of score WITHOUT SPACE is total score for 3 darts and program skip throw(s) but always count 3 darts thrown ):")
    print(" ")
elif rules == "n" or rules == "N" or rules == "no" or rules == "No":
    print ("Good luck!")
    print (" ")

while True:
    try:
        player_count = int(input("Enter player count 1 or 2: "))
    except ValueError:
        print("You can only enter a number 1 or 2")
    else:
        if player_count == 1 or player_count == 2:
            break
        else:
            print("You can only play with 1 or 2 players")


darts_count = 0
total_dart_score = 0

if player_count == 1:
    ask = int(input("Enter starting score: "))

    # peruspelin loop
    while True:
        # Toteuttaa funtion points_counter ja palauttaa sieltä saadut arvot
        round_points, darts_thrown = points_counter()

        # päivittää heitettyt pisteet ja heitetyt tikat
        total_dart_score += round_points
        darts_count += darts_thrown

        # laskee jäjelle jäävät pisteet
        score_left = ask - total_dart_score

        if score_left <= 170: #jos pisteet ovat alle 170, palautetaan suosituksen heitoista joilla voi voittaa pelin
            recommendation = checkout_recommendation(score_left)
            if recommendation:
                print("Recomendations:") # Käytetään silmukkaa tulostamaan suositukset allekkain
                for outcome in recommendation:
                    print(outcome)
        else:
            print("Ei mahdollisia suosituksia tälle pisteelle.")

        if score_left == 0:
            print(f"Good job, you have thrown a total of {darts_count} darts")
            break 
        elif score_left < 0 or score_left == 1: # Tarkistetaan meneekö heitetty tulos alle 0 tai on 1
            total_dart_score -= round_points # Poistetaan heitetty tulos
            print(f"You have overscored! You have points left: {ask - total_dart_score}")
            print(f"Total number of darts thrown: {darts_count}")
        else:
            print(f"You have points left: {score_left}")
            print(f"Total number of darts thrown: {darts_count}")



if player_count == 2:

    darts_count_1 = 0
    total_dart_score_1 = 0
    darts_count_2 = 0
    total_dart_score_2 = 0
    ask_2 = 0

    ask_1 = int(input("Enter starting score: "))
    ask_2 = ask_1

    while True:  # perus pelin loop kolmelle heitetylle tikalle ja 2 pelaajalle 

        round_points_1 = 0  # nollataan pelaaja 1 kierroksen pisteet
        round_points_2 = 0  # nollataan pelaaja 2 kierroksen pisteet

        # pelaaja 1 vuoro
        for i in range(1, 4):
            one_dart_score_1 = input(f"Enter Player 1 {i}. dart score: ")
            if one_dart_score_1 == "":
                continue
            elif one_dart_score_1.startswith("d"):
                one_dart_score_1 = int(one_dart_score_1[1:]) 
                round_points_1 += one_dart_score_1
                darts_count_1 += 4 - i
                break
            else:
                one_dart_score_1 = int(one_dart_score_1)
                darts_count_1 += 1
                round_points_1 += one_dart_score_1  # Fixed line

        total_dart_score_1 += round_points_1
        score_left_1 = ask_1 - total_dart_score_1

        if score_left_1 == 0:
            print(f"Good job, Player 1! You have thrown a total of {darts_count_1} darts.")
            break
        elif score_left_1 < 0 or score_left_1 == 1:
            total_dart_score_1 -= round_points_1
            print(f"You have overscored! You have points left: {ask_1 - total_dart_score_1}")
            print(f"Total number of darts thrown: {darts_count_1}")
        else:
            print(f"You have points left: {score_left_1}")
            print(f"Total number of darts thrown: {darts_count_1}")

        # pelaaaja 2 vuoro
        for i in range(1, 4):
            one_dart_score_2 = input(f"Enter Player 2 {i}. dart score: ")
            if one_dart_score_2 == "":
                continue
            elif one_dart_score_2.startswith("d"):
                one_dart_score_2 = int(one_dart_score_2[1:]) 
                round_points_2 += one_dart_score_2
                darts_count_2 += 4 - i
                break
            else:
                one_dart_score_2 = int(one_dart_score_2)
                darts_count_2 += 1
                round_points_2 += one_dart_score_2

        total_dart_score_2 += round_points_2
        score_left_2 = ask_2 - total_dart_score_2

        if score_left_2 == 0:
            print(f"Good job, Player 2! You have thrown a total of {darts_count_2} darts.")
            break
        elif score_left_2 < 0 or score_left_2 == 1:
            total_dart_score_2 -= round_points_2
            print(f"You have overscored! You have points left: {ask_2 - total_dart_score_2}")
            print(f"Total number of darts thrown: {darts_count_2}")
        else:
            print(f"You have points left: {score_left_2}")
            print(f"Total number of darts thrown: {darts_count_2}")

