import tkinter as tk

# gets the results then puts displays them using labels
def disp_results(results):
    lbl = tk.Label(results, text="This action returns a list of the potenital good investments")
    lbl.pack()
    result_lbls.append(lbl)

    back_button.pack()

    controls.pack_forget()
    results.pack(padx=20, pady=20)

# goes back to the controls frame
def back():
    back_button.pack_forget()
    for i in range(len(result_lbls)):
        result_lbls[i].destroy()

    results.pack_forget()
    controls.pack(padx=50, pady=50)

def success_back():
    success_frame.pack_forget()
    controls.pack(padx=50, pady=50)

def update():
    success_frame.pack(padx=20, pady=20)
    controls.pack_forget()

# creates the window
root = tk.Tk()

# a variable to hold the result labels and buttons
result_lbls = []

# the three frames that the user can be on
controls = tk.Frame(root)
results = tk.Frame(root)
success_frame = tk.Frame(root)

# creates the buttons to switch between the frames
predict_button = tk.Button(controls, text="Predict", command=lambda: disp_results(results))
update_db_button = tk.Button(controls, text="Update Database", command=update)
back_button = tk.Button(results, text="Back", command=back)
success_lbl = tk.Label(success_frame, text="This action pulls Bright MLS listing data to analyze")
success_btn = tk.Button(success_frame, text="Back", command=success_back)

# packs all of the widgets
predict_button.pack(pady=10)
update_db_button.pack(pady=10)
success_lbl.pack()
success_btn.pack()

controls.pack(padx=50, pady=50)

root.mainloop()
