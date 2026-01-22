# perus pelin loop kolmelle heitetylle tikalle ja 1 pelaajalle
def points_counter():
  darts_count = 0
  round_points = 0 # nollataan kunkin kierroksen pisteet

  for i in range(1, 4):
    one_dart_score = input(f"Enter your {i}. dart score: ")

    if one_dart_score == "": #jos syöte on tyhjä niin järjestelmä skippaa sen ja ei lisää Darts_count heitettyä tikkaa
      continue

    elif one_dart_score.startswith("d"): # Jos syöte alkaa d:sta niin skipaan muut heitot ja one_dart_score == round_points

      while True:
        try:
          one_dart_score =int(one_dart_score[1:])
          round_points += one_dart_score
          darts_count += 4 - i
          break
        except ValueError:
          print("Invalid input, please try again, exsample:d<total score>")
          one_dart_score = input(f"Re-enter your total darts score: ")
      break
      

    else: #"perustilanne" jossa yksittäiset heittojen pisteet syötetään yksitellen
      while True:
        try:
          one_dart_score = int(one_dart_score)
          round_points += one_dart_score
          darts_count += 1
          break  # Exit the `while` loop
        except ValueError:
            print("Invalid input, please try again")
            one_dart_score = input(f"Re-enter your {i}. dart score: ")

      
  return round_points, darts_count
