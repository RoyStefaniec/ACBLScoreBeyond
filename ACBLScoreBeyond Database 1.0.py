import tkinter as tk
import psycopg2
import calculate_and_display 
from calculate_and_display import result_var  # Import your scoring function

def calculate_scores(result_var):
    # Use your scoring logic
    base_result = int(result_var)

    if result_var >= 0:
        ns_score = result_var
        ew_score = result_var
    else:
        ns_score = result_var
        ew_score = abs(result_var)
    
    return ns_score, ew_score 

def submit_score ():

    total_score= calculate_and_display.calculate_and_display()
    ns_score, ew_score = calculate_scores(result_var)
    result_var.set(f"NS: {ns_score}, EW: {ew_score}")
    # DB insertion
    conn = psycopg2.connect("dbname=bridge_db user=your_user")
    cur = conn.cursor()
    cur.execute("INSERT INTO scores (ns_score, ew_score) VALUES (%s, %s)", 
                (ns_score, ew_score))
    conn.commit()
    cur.close()
    conn.close()
    
    # Clear entries
    ns_entry.delete(0, tk.END)
    ew_entry.delete(0, tk.END)
    contract_entry.delete(0, tk.END)

root = tk.Tk()

ns_entry = tk.Entry(root)
ew_entry = tk.Entry(root)
contract_entry = tk.Entry(root)
submit = tk.Button(root, text="Submit", command=submit_score)

tk.Label(root, text="NS Tricks:").pack()
ns_entry.pack()
tk.Label(root, text="EW Tricks:").pack()
ew_entry.pack()
tk.Label(root, text="Contract:").pack()
contract_entry.pack()
submit.pack()

root.mainloop()