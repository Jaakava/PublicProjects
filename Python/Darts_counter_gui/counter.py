from checkout_checker import checkout_recommendation
from points_counter import points_counter

def main_game_loop():
    total_dart_score = 0
    darts_count = 0
    
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
            print("")

        if score_left == 0:
            return darts_count
        
        elif score_left < 0 or score_left == 1: # Tarkistetaan meneekö heitetty tulos alle 0 tai on 1
            return ask-total_dart_score, darts_count
        
        else:
            return score_left, darts_count




