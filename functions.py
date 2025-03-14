from curses import window
import json
import datetime
from tkinter import Tk, messagebox
import tkinter

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
    training_data = {
        "datums": date,
        "vingrinājums": exercise,
        "komplekti": sets,
        "atkārtojumi": reps,
        "svars": weight,
        "piezīmes": comments
    }

    try:
        with open("training_data.json", "r") as file:
            all_trainings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_trainings = []

    all_trainings.append(training_data)

    with open("training_data.json", "w") as file:
        json.dump(all_trainings, file, indent=4)

    messagebox.showinfo("Veiksmīgi", "Treniņš veiksmīgi pievienots!")
# Funkcija, lai skatītos iepriekšējos treniņus
def view_trainings():
    try:
        with open("training_data.json", "r") as file:
            all_trainings = json.load(file)
            if not all_trainings:
                messagebox.showinfo("Brīdinājums", "Nav pieejami treniņu dati!")
                return

            view_window = Tk.Toplevel(window)
            view_window.title("Iepriekšējie treniņi")
            for i, training in enumerate(all_trainings, 1):
                tkinter.Label(view_window, text=f"{i}. {training['datums']}: {training['vingrinājums']} ({training['komplekti']} komplekti, {training['atkārtojumi']} atkārtojumi, {training['svars']} kg)").pack()

    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning("Brīdinājums", "Nav pieejami treniņu dati!")

# Funkcija, lai iegūtu ieteikumu nākamajam treniņam

# Funkcija, lai rediģētu treniņu

# Funkcija, lai dzēstu treniņu

# Funkcija, lai parādītu statistiku par treniņiem

# Funkcija, lai veiktu treniņu vēstures meklēšanu