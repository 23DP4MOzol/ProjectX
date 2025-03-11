import tkinter as tk
from tkinter import messagebox
from functions import add_training, view_trainings, edit_training, delete_training, show_statistics, search_trainings, get_recommendation

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

# Funkcijas saistīšana ar pogām
tk.Button(window, text="Pievienot treniņu", command=lambda: add_training(date_entry, exercise_entry, sets_entry, reps_entry, weight_entry, comments_entry)).grid(row=6, column=0, columnspan=2)
tk.Button(window, text="Rediģēt treniņu", command=edit_training).grid(row=7, column=0, columnspan=2)
tk.Button(window, text="Dzēst treniņu", command=delete_training).grid(row=8, column=0, columnspan=2)
tk.Button(window, text="Skatīt treniņus", command=view_trainings).grid(row=9, column=0, columnspan=2)
tk.Button(window, text="Statistika", command=show_statistics).grid(row=10, column=0, columnspan=2)
tk.Button(window, text="Meklēt treniņus", command=search_trainings).grid(row=11, column=0, columnspan=2)
tk.Button(window, text="Ieteikums nākamajam treniņam", command=get_recommendation).grid(row=12, column=0, columnspan=2)

window.mainloop()
