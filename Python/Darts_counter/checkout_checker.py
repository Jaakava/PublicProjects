
# Määritetään mahdolliset heitot
throw = {
    "S": list(range(1, 21)) + [25] + [50],  # Single: 1-20, Bullseye (25)
    "D": list(range(1, 21)),                # Double: 1-20 (2x), pisteet 2-40
    "T": list(range(1, 21))                 # Triple: 1-20 (3x), pisteet 3-60
}

# Funktio heittoehdotusten löytämiseksi
def checkout_recommendation(score_left):
    ehdotukset = []

    # Yhden heiton yhdistelmät
    for h1 in throw:
        for h1_val in throw[h1]:
            arvo1 = h1_val * (1 if h1 == "S" else 2 if h1 == "D" else 3)
            if arvo1 == score_left and (h1 == "D" or (h1 == "S" and h1_val == 50)):#pakotetaan viimeeistelemään pisteet 0 ja niin että viimeinen heittop on tuplaan tai single 50
                ehdotukset.append(f"{h1}{h1_val}")
    
    # Kahden heiton yhdistelmät
    for h1 in throw:
        for h1_val in throw[h1]:#tarkistetaan mahdolliset heitot 1. tikalle ja katsotaan että pisteet on alle score_left
            arvo1 = h1_val * (1 if h1 == "S" else 2 if h1 == "D" else 3)
            if arvo1 >= score_left:
                continue

            if h1 not in ["S", "T"]: #aloituksen olatava sigle tai tripla. tuplaa ei sallita
                continue

            if h1_val <= 18:
                continue

            for h2 in throw:
                for h2_val in throw[h2]:#tarkistetaan mahdolliset heitot 2. tikalle ja katsotaan että pisteet (heito1 + heitto2) on score_left
                    arvo2 = arvo1 + h2_val * (1 if h2 == "S" else 2 if h2 == "D" else 3)
                    if arvo2 == score_left and (h2 == "D" or (h2 == "S" and h2_val == 50)):#pakotetaan viimeeistelemään pisteet 0 ja niin että viimeinen heittop on tuplaan tai single 50
                        ehdotukset.append(f"{h1}{h1_val}, {h2}{h2_val}")
    
    # Kolmen heiton yhdistelmät
    for h1 in throw: #tarkistetaan mahdolliset heitot 1. tikalle ja katsotaan että pisteet on alle score_left
        for h1_val in throw[h1]:
            arvo1 = h1_val * (1 if h1 == "S" else 2 if h1 == "D" else 3)
            if arvo1 >= score_left:
                continue

            if h1 not in ["S", "T"]: #aloituksen olatava sigle tai tripla. tuplaa ei sallita
                continue

            if h1_val <= 18: # ensimmäisen heiton ehdotuksen on oltava enemmän kuin 10
                continue

            if h1_val == 50 or h1_val == 25:
                continue

            for h2 in throw:#tarkistetaan mahdolliset heitot 2. tikalle ja katsotaan että pisteet (heito1 + heitto2) on alle score_left
                for h2_val in throw[h2]:
                    arvo2 = arvo1 + h2_val * (1 if h2 == "S" else 2 if h2 == "D" else 3)
                    if arvo2 >= score_left:
                        continue

                    if h2 not in ["S", "T"]:
                        continue

                    if h2_val <= 15: # toisen heiton ehdotuksen on oltava enemmän kuin 10
                        continue

                    for h3 in throw:#tarkistetaan mahdolliset heitot 3. tikalle ja katsotaan että pisteet (heito1 + heitto2 +heitto3) on score_left
                        for h3_val in throw[h3]:
                            arvo3 = arvo2 + h3_val * (1 if h3 == "S" else 2 if h3 == "D" else 3)
                            if arvo3 == score_left and (h3 == "D" or (h3 == "S" and h3_val == 50)): #pakotetaan viimeeistelemään pisteet 0 ja niin että viimeinen heittop on tuplaan tai single 50
                                ehdotukset.append(f"{h1}{h1_val}, {h2}{h2_val}, {h3}{h3_val}")
                        
    return ehdotukset