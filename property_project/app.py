import tkinter as tk
import sqlite3
import predictor
from database import get_data, update_db, util

def block(base):
    con = sqlite3.connect('database/properties.db')
    cur = con.cursor()

    get_data.block(cur, con, base)

    con.close()

# gets the results then puts displays them using labels
def disp_results(results):
    props = predictor.predict()

    r = 1
    for prop in props:
        btn = tk.Button(results, text="Block", command=lambda: block(prop))
        n = util.float_to_str(round(prop[1], 0))
        lbl = tk.Label(results, text=prop[0][4] + ": " + n)
        btn.grid(row=r, column=0)
        lbl.grid(row=r, column=1)
        result_lbls.append(lbl)
        result_btns.append(btn)
        r += 1

    controls.pack_forget()
    results.grid(padx=20, pady=20)

# goes back to the controls frame
def back():
    for i in range(len(result_lbls)):
        result_lbls[i].destroy()
        result_btns[i].destroy()

    results.grid_forget()
    controls.pack(padx=50, pady=50)

def success_back():
    success_frame.pack_forget()
    controls.pack(padx=50, pady=50)

def update():
    update_db.update()

    success_frame.pack()
    controls.pack_forget()

# creates the window
root = tk.Tk()

# a variable to hold the result labels and buttons
result_lbls = []
result_btns = []

# the three frames that the user can be on
controls = tk.Frame(root)
results = tk.Frame(root)
success_frame = tk.Frame(root)

# creates the buttons to switch between the frames
predict_button = tk.Button(controls, text="Predict", command=lambda: disp_results(results))
update_db_button = tk.Button(controls, text="Update Database", command=update)
back_button = tk.Button(results, text="Back", command=back)
success_lbl = tk.Label(success_frame, text="Success!")
success_btn = tk.Button(success_frame, text="Back", command=success_back)

# packs all of the widgets
predict_button.pack(pady=10)
update_db_button.pack(pady=10)
back_button.grid(row=0, column=0, columnspan=2)
success_lbl.pack()
success_btn.pack()

controls.pack(padx=50, pady=50)

root.mainloop()
