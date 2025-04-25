import json
from tkinter import messagebox
import matplotlib.pyplot as plt

# ✨ Faila nosaukums, kur tiks glabāti visi treniņu dati
TRAINING_FILE = "training_data.json"

# Ielādējam visus treniņus no JSON faila
def load_trainings():
    try:
        with open(TRAINING_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Saglabājam treniņus JSON failā
def save_trainings(trainings):
    with open(TRAINING_FILE, "w", encoding="utf-8") as file:
        json.dump(trainings, file, indent=4)

# Pievienojam jaunu treniņu
def add_training(training):
    all_trainings = load_trainings()
    new_id = len(all_trainings) + 1
    training_data = {
        "id": new_id,
        "datums": training["datums"],
        "vingrinājums": training["vingrinājums"],
        "komplekts": training["komplekts"],
        "atkārtojumi": training["atkārtojumi"],
        "svars": training["svars"],
        "piezīmes": training["piezīmes"]
    }
    all_trainings.append(training_data)
    save_trainings(all_trainings)
    messagebox.showinfo("Veiksmīgi pievienots", "Treniņš veiksmīgi pievienots!")

# Apskatīt visus treniņus
def view_trainings():
    return load_trainings()

# Funkcija treniņa datu rediģēšanai
def edit_training(training_id, datums, vingrinajums, komplekts, atkārtojumi, svars, piezīmes):
    # Iegūstam visus treniņus no datnes vai saraksta
    all_trainings = load_trainings()  # Piemēram, ja dati ir saglabāti failā

    # Atrodam treniņu pēc ID un atjaunojam tā datus
    for training in all_trainings:
        if training["id"] == training_id:
            training["datums"] = datums
            training["vingrinājums"] = vingrinajums
            training["komplekts"] = komplekts
            training["atkārtojumi"] = atkārtojumi
            training["svars"] = svars
            training["piezīmes"] = piezīmes
            break
    else:
        print(f"Treniņš ar ID {training_id} netika atrasts.")
        return False
    
    # Saglabājam visus datus atpakaļ
    save_trainings(all_trainings)
    return True  # Veiksmīgi saglabāts

# Dzēst treniņu
def delete_training(training_id):
    all_trainings = load_trainings()
    all_trainings = [training for training in all_trainings if training["id"] != training_id]
    save_trainings(all_trainings)
    messagebox.showinfo("Veiksmīgi dzēsts", "Treniņš veiksmīgi dzēsts!")

# Meklēt treniņus pēc datuma
def search_trainings(date):
    all_trainings = load_trainings()
    found_trainings = [training for training in all_trainings if training["datums"] == date]
    
    if found_trainings:
        messagebox.showinfo("Meklēt treniņus", f"Treniņi atrasti:\n" + "\n".join([f"{training['datums']} - {training['vingrinājums']}" for training in found_trainings]))
    else:
        messagebox.showinfo("Meklēt treniņus", "Nav atrasti treniņi ar norādīto datumu.")

# Parādīt statistiku (kopējie treniņi, vidējais svars utt.)
def show_statistics():
    all_trainings = load_trainings()
    if not all_trainings:
        messagebox.showinfo("Statistika", "Nav pieejami treniņi.")
        return

    total_trainings = len(all_trainings)
    total_weight = sum([float(training["svars"]) for training in all_trainings if training["svars"].replace(".", "").isdigit()])
    average_weight = total_weight / total_trainings if total_trainings > 0 else 0

    stats_message = (
        f"📊 Treniņi kopā: {total_trainings}\n"
        f"🏋‍♂️ Kopējais svars: {total_weight:.2f} kg\n"
        f"⚖️ Vidējais svars: {average_weight:.2f} kg"
    )

    # Parādīsim statistiku
    messagebox.showinfo("Statistika", stats_message)

    # Diagramma - svaru attēlojums
    weights = [float(training["svars"]) for training in all_trainings if training["svars"].replace(".", "").isdigit()]
    dates = [training["datums"] for training in all_trainings]

    # Izveidojam diagrammu
    plt.figure(figsize=(10, 6))
    plt.plot(dates, weights, marker='o', linestyle='-', color='b', label="Svars")
    plt.xlabel('Datums')
    plt.ylabel('Svars (kg)')
    plt.title('Svara progresss laika gaitā')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

# Iegūt ieteikumu nākamajam treniņam, pamatojoties uz vidējo paceltā svara

def get_recommendation():
    all_trainings = load_trainings()
    if not all_trainings:
        messagebox.showinfo("Ieteikums", "Nav pietiekami daudz datu, lai sniegtu ieteikumus.")
        return

    total_weight = sum([float(training["svars"]) for training in all_trainings if training["svars"].replace(".", "").isdigit()])
    total_trainings = len(all_trainings)
    average_weight = total_weight / total_trainings if total_trainings > 0 else 0

    if average_weight < 50:
        recommendation = "Ieteikums: Mēģiniet palielināt svaru, lai izaicinātu muskuļus!"
    elif average_weight < 100:
        recommendation = "Ieteikums: Lieliski! Turpiniet tādā pašā garā!"
    elif average_weight < 150:
        recommendation = "Ieteikums: Lielisks progress! Iespējams, ka ir vērts koncentrēties uz spēka attīstību."
    else:
        recommendation = "Ieteikums: Tu esi sasniedzis izcilus rezultātus! Pārdomā spēka treniņu uzlabošanu vai palielinājumu."

    messagebox.showinfo("Ieteikums nākamajam treniņam", recommendation)


# Atvērt treniņa rediģēšanas logu
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functions import load_trainings, save_trainings, edit_training

def open_edit_training_window(root, training_id):
    # Ielādējam visus treniņus no faila
    all_trainings = load_trainings()

    # Atrodam konkrēto treniņu pēc ID
    training = None
    for t in all_trainings:
        if t["id"] == training_id:
            training = t
            break

    if not training:
        messagebox.showerror("Kļūda", "Treniņš netika atrasts.")
        return

    # Atveram jaunu logu ar treniņa datiem
    edit_window = tk.Toplevel(root)
    edit_window.title(f"Rediģēt treniņu {training_id}")

    # Ievades lauki treniņa datiem
    tk.Label(edit_window, text="Datums").grid(row=0, column=0)
    datums_entry = tk.Entry(edit_window)
    datums_entry.insert(0, training["datums"])
    datums_entry.grid(row=0, column=1)

    tk.Label(edit_window, text="Vingrinājums").grid(row=1, column=0)
    vingrinajums_entry = tk.Entry(edit_window)
    vingrinajums_entry.insert(0, training["vingrinājums"])
    vingrinajums_entry.grid(row=1, column=1)

    tk.Label(edit_window, text="Komplekts").grid(row=2, column=0)
    komplekts_entry = tk.Entry(edit_window)
    komplekts_entry.insert(0, training["komplekts"])
    komplekts_entry.grid(row=2, column=1)

    tk.Label(edit_window, text="Atkārtojumi").grid(row=3, column=0)
    atkārtojumi_entry = tk.Entry(edit_window)
    atkārtojumi_entry.insert(0, training["atkārtojumi"])
    atkārtojumi_entry.grid(row=3, column=1)

    tk.Label(edit_window, text="Svars").grid(row=4, column=0)
    svars_entry = tk.Entry(edit_window)
    svars_entry.insert(0, training["svars"])
    svars_entry.grid(row=4, column=1)

    tk.Label(edit_window, text="Piezīmes").grid(row=5, column=0)
    piezimes_entry = tk.Entry(edit_window)
    piezimes_entry.insert(0, training["piezīmes"])
    piezimes_entry.grid(row=5, column=1)

    # Saglabāt izmaiņas
    def save_changes():
        new_datums = datums_entry.get()
        new_vingrinajums = vingrinajums_entry.get()
        new_komplekts = komplekts_entry.get()
        new_atkartojumi = atkārtojumi_entry.get()
        new_svars = svars_entry.get()
        new_piezimes = piezimes_entry.get()

        # Nododam izmaiņas atpakaļ uz rediģēšanas funkciju
        edit_training(training_id, new_datums, new_vingrinajums, new_komplekts, new_atkartojumi, new_svars, new_piezimes)

        messagebox.showinfo("Veiksmīgi saglabāts", "Treniņš veiksmīgi rediģēts!")
        edit_window.destroy()  # Aizveram logu pēc saglabāšanas

    # Saglabāšanas poga
    save_button = tk.Button(edit_window, text="Saglabāt", command=save_changes)
    save_button.grid(row=6, column=0, columnspan=2)
