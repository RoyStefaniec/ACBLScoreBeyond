import tkinter as tk
from tkinter import ttk
import pandas as pd
import calculate_bridge_score

# Initialize global variables
final_score = 0
df = pd.DataFrame(columns=['User', 'Score'])

def submit():
    global final_score
    
    # Extract values from inputs
    level = int(contract_level_var.get())
    suit = contract_suit_var.get()
    tricks = int(tricks_taken_var.get())
    vulnerable = vul_var.get() == "Yes"
    
    # Determine contract type
    if level < 3 or (level == 3 and suit != "No Trump"):
        contract_type = "part_score"
    elif level == 3 and suit == "No Trump":
        contract_type = "game"
    elif level < 4:
        contract_type = "part_score"
    elif level == 4 or level == 5:
        contract_type = "game"
    elif level == 6:
        contract_type = "small_slam"
    else:  # level == 7
        contract_type = "grand_slam"

    # Calculate score
    final_score = calculate_bridge_score.calculate_bridge_score(level, suit, tricks, vulnerable)
    
    # Update result label
    result_label.config(text="Score: " + str(final_score))

def submit_score():
    global df
    user = player_entry.get()
    new_row = {'User': user, 'Score': final_score}

    # Using loc to insert the new row efficiently
    df.loc[len(df.index)] = new_row
    
    print(df)

# Creating the main window
root = tk.Tk()
root.title("Bridge Score Calculator")
root.geometry("600x400")

contract_level_var = tk.StringVar()
contract_suit_var = tk.StringVar()
tricks_taken_var = tk.StringVar()
vul_var = tk.StringVar()

# Defining UI elements
tk.Label(root, text="Contract Level:").pack()
tk.OptionMenu(root, contract_level_var, *[str(n) for n in range(1, 8)]).pack()

tk.Label(root, text="Contract Suit:").pack()
tk.OptionMenu(root, contract_suit_var, "Clubs", "Diamonds", "Hearts", "Spades", "No Trump").pack()

tk.Label(root, text="Tricks Taken:").pack()
tk.OptionMenu(root, tricks_taken_var, *[str(n) for n in range(0, 14)]).pack()

tk.Label(root, text="Vulnerable:").pack()
tk.OptionMenu(root, vul_var, "Yes", "No").pack()

tk.Button(root, text="Calculate Score", command=submit).pack()

result_label = tk.Label(root, text="Score: " + str(final_score))
result_label.pack()

# Label for player names
player_label = tk.Label(root, text="Player Names:")
player_label.pack()

# Entry field for player names
player_entry = tk.Entry(root)
player_entry.pack()

# Label for round
round_label = tk.Label(root, text="Round:")
round_label.pack()

# Dropdown menu for round selection
round_var = tk.StringVar(root)
round_var.set("Select Round")  # default value
round_dropdown = tk.OptionMenu(root, round_var, "1", "2", "3", "4")
round_dropdown.pack()

# Submit Score button
submit_btn = tk.Button(root, text="Submit Score", command=submit_score)
submit_btn.pack()

# Run the main loop
root.mainloop()
