import json
from tkinter import messagebox
from datetime import datetime
import os  # Pievienots os modulis

# Function to ensure the training file exists
def ensure_file_exists():
    print("Pārbauda, vai fails pastāv...")
    if not os.path.exists('training_data.json'):
        with open('training_data.json', 'w', encoding='utf-8') as f:
            json.dump([], f)  # Create an empty list if the file doesn't exist
    else:
        print("Fails jau pastāv.")

# Function to add a new training
def add_training(date_entry, exercise_entry, sets_entry, reps_entry, weight_entry, comments_entry):
    ensure_file_exists()  # Ensure the file exists before writing to it
    new_training = {
        "id": len(view_trainings()) + 1,
        "datums": date_entry,
        "vingrinājums": exercise_entry,
        "komplekts": sets_entry,
        "atkārtojumi": reps_entry,
        "svars": weight_entry,
        "piezīmes": comments_entry
    }

    try:
        with open('training_data.json', 'a', encoding='utf-8') as file:
            json.dump(new_training, file)
            file.write("\n")
        print(f"Treniņš pievienots: {new_training}")  # Paziņojums, kas parāda pievienoto treniņu
        messagebox.showinfo("Veiksmīgi", "Treniņš veiksmīgi pievienots!")
    except Exception as e:
        messagebox.showerror("Kļūda", f"Treniņu pievienošana neizdevās: {e}")

# Function to view all trainings
def view_trainings():
    ensure_file_exists()  # Ensure the file exists before reading it

    try:
        with open('training_data.json', 'r', encoding='utf-8') as file:
            content = file.read().strip()
            print(f"Fails saturs pirms nolasīšanas: {content}")  # Parādām faila saturu

            if not content:
                print("Fails ir tukšs vai satur nederīgus datus!")  # Paziņojums par tukšu failu
                messagebox.showinfo("Treniņi", "Fails ir tukšs vai satur nederīgus datus!")
                return []

            # Tagad nolasām visu failu kā JSON masīvu
            try:
                all_trainings = json.loads(content)  # Nolasām visu saturu kā JSON objektu
                print(f"Visi treniņi pēc nolasīšanas: {all_trainings}")  # Paziņojums, kas parāda visus treniņus
                return all_trainings
            except json.JSONDecodeError:
                print("Kļūda, nolasot treniņu datus.")  # Paziņojums par kļūdu nolasot
                messagebox.showerror("Kļūda", "Kļūda, nolasot treniņu datus.")
                return []
    except FileNotFoundError:
        print("Fails netika atrasts.")  # Paziņojums par to, ka fails netika atrasts
        messagebox.showerror("Kļūda", "Treniņu dati netika atrasti.")
        return []


# Function to edit a training
def edit_training(training_id, date, exercise, sets, reps, weight, notes):
    all_trainings = view_trainings()
    training_to_edit = next((t for t in all_trainings if t['id'] == training_id), None)

    if training_to_edit:
        training_to_edit["datums"] = date
        training_to_edit["vingrinājums"] = exercise
        training_to_edit["komplekts"] = sets
        training_to_edit["atkārtojumi"] = reps
        training_to_edit["svars"] = weight
        training_to_edit["piezīmes"] = notes

        with open('training_data.json', 'w') as file:
            for training in all_trainings:
                json.dump(training, file)
                file.write("\n")
        messagebox.showinfo("Veiksmīgi", "Treniņš veiksmīgi rediģēts!")
    else:
        messagebox.showerror("Kļūda", "Treniņš ar norādīto ID nav atrasts.")

# Function to delete a training
def delete_training(training_id):
    all_trainings = view_trainings()
    training_to_delete = next((t for t in all_trainings if t['id'] == training_id), None)

    if training_to_delete:
        all_trainings = [t for t in all_trainings if t['id'] != training_id]

        with open('training_data.json', 'w') as file:
            for training in all_trainings:
                json.dump(training, file)
                file.write("\n")
        messagebox.showinfo("Veiksmīgi", "Treniņš veiksmīgi izdzēsts!")
    else:
        messagebox.showerror("Kļūda", "Treniņš ar norādīto ID nav atrasts.")

# Function to search trainings by date
def search_trainings(date):
    all_trainings = view_trainings()
    found_trainings = [training for training in all_trainings if training["datums"] == date]

    if found_trainings:
        for training in found_trainings:
            print(f"ID: {training['id']}, {training['datums']} - {training['vingrinājums']}")
    else:
        messagebox.showinfo("Meklēšana", "Nav atrasti treniņi ar šo datumu.")

# Function to show training statistics
def show_statistics():
    all_trainings = view_trainings()
    if not all_trainings:
        messagebox.showinfo("Statistika", "Nav pieejami treniņi.")
        return

    total_trainings = len(all_trainings)
    total_sets = sum(int(training["komplekts"]) for training in all_trainings)
    total_reps = sum(int(training["atkārtojumi"]) for training in all_trainings)
    total_weight = sum(float(training["svars"]) for training in all_trainings)

    avg_weight = total_weight / total_trainings if total_trainings else 0
    avg_sets = total_sets / total_trainings if total_trainings else 0
    avg_reps = total_reps / total_trainings if total_trainings else 0

    stats = (
        f"Total Treniņi: {total_trainings}\n"
        f"Vidējais svars: {avg_weight:.2f} kg\n"
        f"Vidējais komplekti: {avg_sets:.2f}\n"
        f"Vidējais atkārtojumi: {avg_reps:.2f}\n"
        f"Total komplekti: {total_sets}\n"
        f"Total atkārtojumi: {total_reps}\n"
        f"Total svars: {total_weight:.2f} kg"
    )

    messagebox.showinfo("Statistika", stats)

# Function to get a training recommendation
def get_recommendation():
    all_trainings = view_trainings()
    if not all_trainings:
        messagebox.showinfo("Ieteikums", "Nav pieejami treniņi.")
        return

    latest_training = max(all_trainings, key=lambda x: datetime.strptime(x["datums"], "%Y-%m-%d"))
    recommended_exercise = latest_training["vingrinājums"]

    messagebox.showinfo("Ieteikums", f"Ņemot vērā jūsu pēdējo treniņu ({latest_training['datums']}), ieteicams turpināt ar vingrinājumu: {recommended_exercise}")
