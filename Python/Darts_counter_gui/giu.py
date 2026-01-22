import tkinter as tk
from tkinter import ttk
from counter import main_game_loop

def button_func(player_count_var, count):
    if count == "2":
        # jos player count on 2 tulee "Coming soon!" teksti
        message_label.config(text="Coming soon! :)")
    else:
        # Jos player count on 1 niin tyhjä teksti
        message_label.config(text="Player count set to 1")
    player_count_var.set(count)
    print(f"Player count set to {count}")  # mahdollinen piiloviesti konsolissa debuggausta varten

# tehdään tkinter ikkunan
window = tk.Tk()
window.title("Darts Counter")
window.geometry("400x800")

# Define a StringVar to display and hold the player count
player_count_var = tk.StringVar(value="1")  # Default player count


# Label to display the "Coming soon!" message when 2 Players is selected
message_label = ttk.Label(window, text="")
message_label.pack()

# Button to set player count to 1
button_1_player = ttk.Button(window, text="1 Player", command=lambda: button_func(player_count_var, "1"))
button_1_player.pack()

# Button to set player count to 2
button_2_players = ttk.Button(window, text="2 Players", command=lambda: button_func(player_count_var, "2"))
button_2_players.pack()

# Main program loop
window.mainloop()
