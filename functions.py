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
def get_recommendation():
    try:
        with open("training_data.json", "r") as file:
            all_trainings = json.load(file)
            if not all_trainings:
                messagebox.showinfo("Brīdinājums", "Nav pieejami treniņu dati!")
                return

            last_training = all_trainings[-1]
            recommended_weight = float(last_training['svars']) * 1.05  # Palielina svaru par 5%

            messagebox.showinfo("Ieteikums", f"Ieteiktais svars nākamajam treniņam: {recommended_weight:.2f} kg")

    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning("Brīdinājums", "Nav pieejami treniņu dati!")

# Funkcija, lai rediģētu treniņu
def edit_training():
    try:
        with open("training_data.json", "r") as file:
            all_trainings = json.load(file)
            # Ja nav treniņu datu
            if not all_trainings:
                messagebox.showinfo("Brīdinājums", "Nav pieejami treniņu dati!")
                return

            # Pārbaudīt, vai lietotājs izvēlējās treniņu
            training_index = int(input("Izvēlies treniņa numuru, kuru vēlies rediģēt: ")) - 1
            if training_index < 0 or training_index >= len(all_trainings):
                messagebox.showerror("Kļūda", "Nederīgs treniņa numurs!")
                return

            selected_training = all_trainings[training_index]
            new_weight = input(f"Jaunais svars (kg) ({selected_training['svars']}): ")
            new_sets = input(f"Jauni komplekti ({selected_training['komplekti']}): ")
            new_reps = input(f"Jauni atkārtojumi ({selected_training['atkārtojumi']}): ")

            selected_training['svars'] = float(new_weight if new_weight else selected_training['svars'])
            selected_training['komplekti'] = int(new_sets if new_sets else selected_training['komplekti'])
            selected_training['atkārtojumi'] = int(new_reps if new_reps else selected_training['atkārtojumi'])

            with open("training_data.json", "w") as file:
                json.dump(all_trainings, file, indent=4)

            messagebox.showinfo("Veiksmīgi", "Treniņš veiksmīgi rediģēts!")

    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning("Brīdinājums", "Nav pieejami treniņu dati!")

# Funkcija, lai dzēstu treniņu

# Funkcija, lai parādītu statistiku par treniņiem

# Funkcija, lai veiktu treniņu vēstures meklēšanu