import tkinter as tk
from tkinter import ttk
import get_score
import get_basescore

def calculate_and_display():

    is_vulnerable = vulnerable_var.get()
    doubled = double_var.get()
    redoubled = redouble_var.get()
    base_points = get_basescore.get_basescore(contract_level_entry.get(), tricks_taken_entry.get(), suit_combobox.get(), is_vulnerable, doubled, redoubled)   
    score = get_score.get_score(contract_level_entry.get(), tricks_taken_entry.get(), suit_combobox.get(), is_vulnerable, doubled, redoubled)
    total_score = base_points + score
    result_var.set(f"The bridge score is: {total_score}")


app = tk.Tk()
app.title("Bridge Score Calculator")

#Contract level entry

tk.Label(app, text="Contract Level").grid(row=0, column=0)
contract_level_entry = ttk.Combobox(app, values=["1","2","3","4","5","6","7"])
contract_level_entry.grid(row=0, column=1)

#Tricks taken entry

tk.Label(app, text="Tricks Taken").grid(row=1, column=0)
tricks_taken_entry = ttk.Combobox(app, values=["0","1","2","3","4","5","6","7","8","9","10","11","12","13"])
tricks_taken_entry.grid(row=1, column=1)

#Suit selection

tk.Label(app, text="Suit").grid(row=2, column=0)
suit_combobox = ttk.Combobox(app, values=["Clubs", "Diamonds", "Hearts", "Spades", "No Trump"])
suit_combobox.grid(row=2, column=1)

#Vulnerability option

vulnerable_var = tk.BooleanVar()
tk.Checkbutton(app, text="Vulnerable", variable=vulnerable_var).grid(row=3, column=0, columnspan=2)

#Double option

double_var = tk.BooleanVar()
tk.Checkbutton(app, text="Double", variable=double_var).grid(row=4, column=0, columnspan=2)

#Redouble option

redouble_var = tk.BooleanVar()
tk.Checkbutton(app, text="Redouble", variable=redouble_var).grid(row=5, column=0, columnspan=2)

#Calculate button

tk.Button(app, text="Calculate Score", command=calculate_and_display).grid(row=6, column=0, columnspan=2)

#Result display

result_var = tk.StringVar()
tk.Label(app, textvariable=result_var).grid(row=7, column=0, columnspan=2)

if __name__ == "__main__":
    app.mainloop()