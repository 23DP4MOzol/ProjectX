import json
import tkinter as tk
from tkinter import messagebox

# Funkcija, lai pievienotu jaunu treniņu
def add_training(date_entry, exercise_entry, sets_entry, reps_entry, weight_entry, comments_entry):
    new_training = {
        "datums": date_entry.get(),
        "vingrinājums": exercise_entry.get(),
        "komplekti": sets_entry.get(),
        "atkārtojumi": reps_entry.get(),
        "svars": weight_entry.get(),
        "piezīmes": comments_entry.get()
    }

    try:
        with open("training_data.json", "r", encoding="utf-8") as file:
            all_trainings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_trainings = []

    all_trainings.append(new_training)

    with open("training_data.json", "w", encoding="utf-8") as file:
        json.dump(all_trainings, file, indent=4)

    messagebox.showinfo("Veiksmīgi pievienots", "Jaunais treniņš ir veiksmīgi pievienots!")

# Funkcija, lai skatītu visus treniņus
def view_trainings():
    try:
        with open("training_data.json", "r", encoding="utf-8") as file:
            all_trainings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_trainings = []

    # Izdrukā visus treniņus
    for training in all_trainings:
        print(f"Datums: {training['datums']}, Vingrinājums: {training['vingrinājums']}, Komplekts: {training['komplekti']}, Atkārtojumi: {training['atkārtojumi']}, Svars: {training['svars']}, Piezīmes: {training['piezīmes']}")

# Funkcija, lai rediģētu esošu treniņu
def edit_training(training_index, date_entry, exercise_entry, sets_entry, reps_entry, weight_entry, comments_entry):
    try:
        with open("training_data.json", "r", encoding="utf-8") as file:
            all_trainings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_trainings = []

    # Rediģē konkrētu treniņu
    all_trainings[training_index]["datums"] = date_entry.get()
    all_trainings[training_index]["vingrinājums"] = exercise_entry.get()
    all_trainings[training_index]["komplekti"] = sets_entry.get()
    all_trainings[training_index]["atkārtojumi"] = reps_entry.get()
    all_trainings[training_index]["svars"] = weight_entry.get()
    all_trainings[training_index]["piezīmes"] = comments_entry.get()

    # Saglabā izmaiņas atpakaļ JSON failā
    with open("training_data.json", "w", encoding="utf-8") as file:
        json.dump(all_trainings, file, indent=4)

    messagebox.showinfo("Veiksmīgi rediģēts", "Treniņš ir veiksmīgi rediģēts!")

# Funkcija, lai izdzēstu treniņu
def delete_training(training_index):
    try:
        with open("training_data.json", "r", encoding="utf-8") as file:
            all_trainings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        all_trainings = []

    # Dzēš izvēlēto treniņu
    all_trainings.pop(training_index)

    # Saglabā izmaiņas atpakaļ JSON failā
    with open("training_data.json", "w", encoding="utf-8") as file:
        json.dump(all_trainings, file, indent=4)

    messagebox.showinfo("Veiksmīgi izdzēsts", "Treniņš ir veiksmīgi izdzēsts!")

# Funkcija, lai parādītu statistiku
def show_statistics():
    try:
        with open("training_data.json", "r", encoding="utf-8") as file:
            all_trainings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning("Brīdinājums", "Nav pieejami treniņu dati!")
        return

    total_weight = 0
    for training in all_trainings:
        total_weight += float(training["svars"])

    messagebox.showinfo("Statistika", f"Kopējais paceltā svara daudzums visos treniņos: {total_weight} kg")

# Funkcija, lai meklētu treniņus pēc datuma
def search_trainings(date):
    try:
        with open("training_data.json", "r", encoding="utf-8") as file:
            all_trainings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning("Brīdinājums", "Nav pieejami treniņu dati!")
        return

    found_trainings = [training for training in all_trainings if training["datums"] == date]
    if found_trainings:
        for training in found_trainings:
            print(f"Datums: {training['datums']}, Vingrinājums: {training['vingrinājums']}, Komplekts: {training['komplekti']}, Atkārtojumi: {training['atkārtojumi']}, Svars: {training['svars']}, Piezīmes: {training['piezīmes']}")
    else:
        messagebox.showinfo("Nav atrasts", f"Nav atrasti treniņi ar datumu: {date}")

# Funkcija, lai saņemtu ieteikumus
def get_recommendation():
    try:
        with open("training_data.json", "r", encoding="utf-8") as file:
            all_trainings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning("Brīdinājums", "Nav pieejami treniņu dati!")
        return

    # Piemērs - ieteikums, ņemot vērā iepriekšējos treniņus
    recommended_exercise = "Squats"  # Dummy recommendation
    messagebox.showinfo("Ieteikums", f"Šis vingrinājums ir ieteikts: {recommended_exercise}")

# Tkinter lietotāja saskarne
def create_gui():
    root = tk.Tk()
    root.title("Treniņu žurnāls")

    # Ievades lauki treniņa pievienošanai
    date_label = tk.Label(root, text="Datums:")
    date_label.pack()
    date_entry = tk.Entry(root)
    date_entry.pack()

    exercise_label = tk.Label(root, text="Vingrinājums:")
    exercise_label.pack()
    exercise_entry = tk.Entry(root)
    exercise_entry.pack()

    sets_label = tk.Label(root, text="Komplekts:")
    sets_label.pack()
    sets_entry = tk.Entry(root)
    sets_entry.pack()

    reps_label = tk.Label(root, text="Atkārtojumi:")
    reps_label.pack()
    reps_entry = tk.Entry(root)
    reps_entry.pack()

    weight_label = tk.Label(root, text="Svars (kg):")
    weight_label.pack()
    weight_entry = tk.Entry(root)
    weight_entry.pack()

    comments_label = tk.Label(root, text="Piezīmes:")
    comments_label.pack()
    comments_entry = tk.Entry(root)
    comments_entry.pack()

    def save_training():
        add_training(date_entry, exercise_entry, sets_entry, reps_entry, weight_entry, comments_entry)

    save_button = tk.Button(root, text="Pievienot treniņu", command=save_training)
    save_button.pack()

    # Poga treniņu skatīšanai
    view_button = tk.Button(root, text="Skatīt treniņus", command=view_trainings)
    view_button.pack()

    # Poga treniņu meklēšanai pēc datuma
    def search_training():
        search_trainings(date_entry.get())

    search_button = tk.Button(root, text="Meklēt treniņus", command=search_training)
    search_button.pack()

    # Poga statistikas skatīšanai
    stats_button = tk.Button(root, text="Skatīt statistiku", command=show_statistics)
    stats_button.pack()

    # Poga ieteikumu saņemšanai
    rec_button = tk.Button(root, text="Saņemt ieteikumu", command=get_recommendation)
    rec_button.pack()

    root.mainloop()

# Palaiž lietotāja saskarni
if __name__ == "__main__":
    create_gui()
