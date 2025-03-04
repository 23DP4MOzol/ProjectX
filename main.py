import tkinter as tk

# Galvenais logs
window = tk.Tk()
window.title("Sporta treniņu plānošanas lietotne")

# Treniņa datu ievades lauki
tk.Label(window, text="Datums (YYYY-MM-DD):").grid(row=0, column=0, sticky="w")
date_entry = tk.Entry(window)
date_entry.grid(row=0, column=1)

tk.Label(window, text="Vingrinājums:").grid(row=1, column=0, sticky="w")
exercise_entry = tk.Entry(window)
exercise_entry.grid(row=1, column=1)

tk.Label(window, text="Komplekti:").grid(row=2, column=0, sticky="w")
sets_entry = tk.Entry(window)
sets_entry.grid(row=2, column=1)

tk.Label(window, text="Atkārtojumi:").grid(row=3, column=0, sticky="w")
reps_entry = tk.Entry(window)
reps_entry.grid(row=3, column=1)

tk.Label(window, text="Svars (kg):").grid(row=4, column=0, sticky="w")
weight_entry = tk.Entry(window)
weight_entry.grid(row=4, column=1)

tk.Label(window, text="Piezīmes:").grid(row=5, column=0, sticky="w")
comments_entry = tk.Entry(window)
comments_entry.grid(row=5, column=1)

# Pogu, lai pievienotu treniņu
add_button = tk.Button(window, text="Pievienot treniņu")
add_button.grid(row=6, column=0, columnspan=2)

# Sākt GUI
window.mainloop()
