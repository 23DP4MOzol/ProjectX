
import json
import datetime
from tkinter import messagebox

# Funkcija, lai pievienotu treniņu
def add_training(date_entry, exercise_entry, sets_entry, reps_entry, weight_entry, comments_entry):
    date = date_entry.get()
    exercise = exercise_entry.get()
    sets = sets_entry.get()
    reps = reps_entry.get()
    weight = weight_entry.get()
    comments = comments_entry.get()

    if not date or not exercise or not sets or not reps or not weight:
        messagebox.showerror("Kļūda", "Lūdzu aizpildiet visus laukus!")
        return

    try:
        
        datetime.datetime.strptime(date, '%Y-%m-%d')
        if datetime.datetime.strptime(date, '%Y-%m-%d') > datetime.datetime.now():
            messagebox.showerror("Kļūda", "Datums nevar būt nākotnē!")
            return
    except ValueError:
        messagebox.showerror("Kļūda", "Nepareizs datuma formāts!")
        return

    try:
        weight = float(weight)
        sets = int(sets)
        reps = int(reps)
        if weight < 0 or sets < 0 or reps < 0:
            raise ValueError("Negatīvi skaitļi nav pieļaujami")
    except ValueError:
        messagebox.showerror("Kļūda", "Svars, komplekti un atkārtojumi jābūt skaitļiem, un tiem jābūt pozitīviem!")
        return
# Saglabāt treniņu datus

# Funkcija, lai skatītos iepriekšējos treniņus

# Funkcija, lai rediģētu treniņu

# Funkcija, lai dzēstu treniņu

# Funkcija, lai parādītu statistiku par treniņiem

# Funkcija, lai veiktu treniņu vēstures meklēšanu