import json
from tkinter import messagebox

# ✨ File to store all training data
TRAINING_FILE = "training_data.json"

# Load all trainings from the JSON file
def load_trainings():
    try:
        with open(TRAINING_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save trainings to the JSON file
def save_trainings(trainings):
    with open(TRAINING_FILE, "w", encoding="utf-8") as file:
        json.dump(trainings, file, indent=4)

# Add a new training
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

# View all trainings
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




# Delete a training
def delete_training(training_id):
    all_trainings = load_trainings()
    all_trainings = [training for training in all_trainings if training["id"] != training_id]
    save_trainings(all_trainings)
    messagebox.showinfo("Veiksmīgi dzēsts", "Treniņš veiksmīgi dzēsts!")

# Search for trainings by date
def search_trainings(date):
    all_trainings = load_trainings()
    found_trainings = [training for training in all_trainings if training["datums"] == date]
    
    if found_trainings:
        messagebox.showinfo("Meklēt treniņus", f"Treniņi atrasti:\n" + "\n".join([f"{training['datums']} - {training['vingrinājums']}" for training in found_trainings]))
    else:
        messagebox.showinfo("Meklēt treniņus", "Nav atrasti treniņi ar norādīto datumu.")

# Show statistics (total trainings, average weight, etc.)
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

    messagebox.showinfo("Statistika", stats_message)

# Get a recommendation for the next training based on average weight lifted
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
    else:
        recommendation = "Ieteikums: Lielisks progress! Iespējams, ka ir vērts koncentrēties uz spēka attīstību."

    messagebox.showinfo("Ieteikums nākamajam treniņam", recommendation)

# Open the edit window for a specific training
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functions import load_trainings, save_trainings, edit_training

def open_edit_training_window(root, training_id):
    # Load all trainings from the file
    all_trainings = load_trainings()

    # Find the specific training by ID
    training = None
    for t in all_trainings:
        if t["id"] == training_id:
            training = t
            break

    if not training:
        messagebox.showerror("Error", "Training not found.")
        return

    # Open a new window with the training data
    edit_window = tk.Toplevel(root)
    edit_window.title(f"Edit Training {training_id}")

    # Entry fields for the training data
    tk.Label(edit_window, text="Date").grid(row=0, column=0)
    datums_entry = tk.Entry(edit_window)
    datums_entry.insert(0, training["datums"])
    datums_entry.grid(row=0, column=1)

    tk.Label(edit_window, text="Exercise").grid(row=1, column=0)
    vingrinajums_entry = tk.Entry(edit_window)
    vingrinajums_entry.insert(0, training["vingrinājums"])
    vingrinajums_entry.grid(row=1, column=1)

    tk.Label(edit_window, text="Sets").grid(row=2, column=0)
    komplekts_entry = tk.Entry(edit_window)
    komplekts_entry.insert(0, training["komplekts"])
    komplekts_entry.grid(row=2, column=1)

    tk.Label(edit_window, text="Reps").grid(row=3, column=0)
    atkārtojumi_entry = tk.Entry(edit_window)
    atkārtojumi_entry.insert(0, training["atkārtojumi"])
    atkārtojumi_entry.grid(row=3, column=1)

    tk.Label(edit_window, text="Weight").grid(row=4, column=0)
    svars_entry = tk.Entry(edit_window)
    svars_entry.insert(0, training["svars"])
    svars_entry.grid(row=4, column=1)

    tk.Label(edit_window, text="Notes").grid(row=5, column=0)
    piezimes_entry = tk.Entry(edit_window)
    piezimes_entry.insert(0, training["piezīmes"])
    piezimes_entry.grid(row=5, column=1)

    # Save changes
    def save_changes():
        new_datums = datums_entry.get()
        new_vingrinajums = vingrinajums_entry.get()
        new_komplekts = komplekts_entry.get()
        new_atkartojumi = atkārtojumi_entry.get()
        new_svars = svars_entry.get()
        new_piezimes = piezimes_entry.get()

        # Pass the changes back to the edit_training function
        edit_training(training_id, new_datums, new_vingrinajums, new_komplekts, new_atkartojumi, new_svars, new_piezimes)

        messagebox.showinfo("Successfully saved", "Training successfully edited!")
        edit_window.destroy()  # Close the window after saving

    # Save button
    save_button = tk.Button(edit_window, text="Save", command=save_changes)
    save_button.grid(row=6, column=0, columnspan=2)
