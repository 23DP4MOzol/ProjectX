import json
from tkinter import messagebox

# Function to add new training
def add_training(date_entry, exercise_entry, sets_entry, reps_entry, weight_entry, comments_entry):
    new_training = {
        "id": str(len(get_all_trainings()) + 1),  # Creating a unique ID based on the length of the current data
        "datums": date_entry.get(),
        "vingrinājums": exercise_entry.get(),
        "komplekts": sets_entry.get(),  # Ensure the key is 'komplekts'
        "atkārtojumi": reps_entry.get(),  # Ensure the key is 'atkārtojumi'
        "svars": weight_entry.get(),
        "piezīmes": comments_entry.get()
    }

    all_trainings = get_all_trainings()

    all_trainings.append(new_training)

    with open("training_data.json", "w", encoding="utf-8") as file:
        json.dump(all_trainings, file, indent=4)

    messagebox.showinfo("Veiksmīgi pievienots", "Jaunais treniņš ir veiksmīgi pievienots!")


# Function to get all trainings
def get_all_trainings():
    try:
        with open("training_data.json", "r", encoding="utf-8") as file:
            all_trainings = json.load(file)
            print("Loaded data:", all_trainings)  # Debugging line to check loaded data
            if all_trainings is None:  # If the loaded data is None, return an empty list
                return []
            return all_trainings
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading training data: {e}")
        return []  # Return an empty list in case of errors



# Function to view all trainings
def view_trainings():
    all_trainings = get_all_trainings()

    if not all_trainings:  # If no trainings are found, return early
        print("Nav atrasti treniņi.")
        return []  # Or return an empty list instead of None
    
    for training in all_trainings:
        if isinstance(training, dict):  # Ensure each training is a dictionary
            datums = training.get('datums', 'N/A')
            vingrinājums = training.get('vingrinājums', 'N/A')
            komplekts = training.get('komplekts', 'N/A')
            atkārtojumi = training.get('atkārtojumi', 'N/A')
            svars = training.get('svars', 'N/A')
            piezīmes = training.get('piezīmes', 'N/A')

            print(f"Datums: {datums}, Vingrinājums: {vingrinājums}, "
                  f"Komplekts: {komplekts}, Atkārtojumi: {atkārtojumi}, "
                  f"Svars: {svars}, Piezīmes: {piezīmes}")
        else:
            print(f"Invalid data: {training}")
    return all_trainings  # Return the list of trainings after printing


# Function to edit a training
def edit_training(training_index, date_entry, exercise_entry, sets_entry, reps_entry, weight_entry, comments_entry):
    all_trainings = get_all_trainings()

    # Edit the specific training
    all_trainings[training_index]["datums"] = date_entry.get()
    all_trainings[training_index]["vingrinājums"] = exercise_entry.get()
    all_trainings[training_index]["komplekti"] = sets_entry.get()
    all_trainings[training_index]["atkārtojumi"] = reps_entry.get()
    all_trainings[training_index]["svars"] = weight_entry.get()
    all_trainings[training_index]["piezīmes"] = comments_entry.get()

    # Save changes back to JSON
    with open("training_data.json", "w", encoding="utf-8") as file:
        json.dump(all_trainings, file, indent=4)

    messagebox.showinfo("Veiksmīgi rediģēts", "Treniņš ir veiksmīgi rediģēts!")

# Function to delete a training
def delete_training(training_index):
    all_trainings = get_all_trainings()

    # Delete the specific training
    all_trainings.pop(training_index)

    # Save changes back to JSON
    with open("training_data.json", "w", encoding="utf-8") as file:
        json.dump(all_trainings, file, indent=4)

    messagebox.showinfo("Veiksmīgi izdzēsts", "Treniņš ir veiksmīgi izdzēsts!")

# Function to show statistics
def show_statistics():
    all_trainings = get_all_trainings()

    total_weight = 0
    for training in all_trainings:
        total_weight += float(training["svars"])

    messagebox.showinfo("Statistika", f"Kopējais paceltā svara daudzums visos treniņos: {total_weight} kg")

# Function to search trainings by date
def search_trainings(date):
    all_trainings = get_all_trainings()

    found_trainings = [training for training in all_trainings if training["datums"] == date]
    if found_trainings:
        for training in found_trainings:
            print(f"Datums: {training['datums']}, Vingrinājums: {training['vingrinājums']}, "
                  f"Komplekts: {training['komplekti']}, Atkārtojumi: {training['atkārtojumi']}, "
                  f"Svars: {training['svars']}, Piezīmes: {training['piezīmes']}")
    else:
        messagebox.showinfo("Nav atrasti treniņi", "Nav atrasti treniņi šajā datumā.")

# Function to get recommendation for the next training
def get_recommendation():
    all_trainings = get_all_trainings()

    if all_trainings:
        last_training = all_trainings[-1]
        messagebox.showinfo("Ieteikums", f"Pamatojoties uz jūsu pēdējo treniņu, "
                                         f"vēlams turpināt strādāt pie vingrinājuma {last_training['vingrinājums']}.")
    else:
        messagebox.showinfo("Nav treniņu", "Nav veikti treniņi, lai ieteiktu nākamo.")

