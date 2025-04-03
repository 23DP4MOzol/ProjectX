import tkinter as tk
from tkinter import ttk, messagebox
from functions import add_training, view_trainings, edit_training, delete_training, show_statistics, search_trainings, get_recommendation

# 🌟 Galvenais logs
window = tk.Tk()
window.title("🏋 Sporta Treniņu Plānošana")
window.geometry("600x550")
window.configure(bg="#1e272e")  # Tumšs fons

# 🎨 Pielāgots GUI stils
style = ttk.Style()
style.theme_use("clam")  # Moderns stils

style.configure("TFrame", background="#1e272e")
style.configure("TLabel", font=("Arial", 12), background="#1e272e", foreground="white")
style.configure("TButton", font=("Arial", 12, "bold"), foreground="white", background="#0984e3", padding=10)
style.map("TButton", background=[("active", "#74b9ff")])  # Hover efekts

# 🌟 FUNKCIJA: Parāda tikai vienu rāmi
def show_frame(frame):
    for f in all_frames:
        f.pack_forget()
    frame.pack(fill="both", expand=True, padx=20, pady=20)

# 🏠 Galvenais sākuma rāmis
home_frame = ttk.Frame(window)
home_frame.pack(fill="both", expand=True)

ttk.Label(home_frame, text="📋 Izvēlies darbību:", font=("Arial", 16, "bold")).pack(pady=20)

# 🎯 Izveido stilīgas pogas
def create_button(text, command):
    return ttk.Button(home_frame, text=text, command=command, width=30)

buttons = [
    ("➕ Pievienot treniņu", lambda: show_frame(add_frame)),
    ("✏ Rediģēt treniņu", lambda: show_frame(edit_frame)),
    ("🗑 Dzēst treniņu", lambda: show_frame(delete_frame)),
    ("📅 Skatīt treniņus", lambda: show_frame(view_frame)),
    ("📊 Statistika", lambda: show_frame(stats_frame)),
    ("🔍 Meklēt treniņus", lambda: show_frame(search_frame)),
    ("💡 Ieteikums nākamajam treniņam", lambda: show_frame(recommend_frame))
]

for text, cmd in buttons:
    create_button(text, cmd).pack(pady=5)

# 📦 Katras sadaļas rāmji
def create_frame():
    return ttk.Frame(window, padding=20)

add_frame = create_frame()
edit_frame = create_frame()
delete_frame = create_frame()
view_frame = create_frame()
stats_frame = create_frame()
search_frame = create_frame()
recommend_frame = create_frame()

all_frames = [home_frame, add_frame, edit_frame, delete_frame, view_frame, stats_frame, search_frame, recommend_frame]

# 🔙 Atpakaļ poga
def create_back_button(frame):
    ttk.Button(frame, text="⬅ Atpakaļ", command=lambda: show_frame(home_frame), width=15).pack(pady=10)

# 🆕 Pievienot treniņu
ttk.Label(add_frame, text="🏋 Pievienot jaunu treniņu", font=("Arial", 16, "bold")).pack(pady=10)

entries = {}
fields = ["📅 Datums (YYYY-MM-DD)", "🏋 Vingrinājums", "🔢 Komplekti", "🔁 Atkārtojumi", "🏋‍♂️ Svars (kg)", "📝 Piezīmes"]

for field in fields:
    ttk.Label(add_frame, text=field).pack(anchor="w")
    entry = ttk.Entry(add_frame, width=30)
    entry.pack(pady=2)
    entries[field] = entry

ttk.Button(add_frame, text="✅ Pievienot", command=lambda: add_training(
    entries["📅 Datums (YYYY-MM-DD)"].get(), entries["🏋 Vingrinājums"].get(),
    entries["🔢 Komplekti"].get(), entries["🔁 Atkārtojumi"].get(),
    entries["🏋‍♂️ Svars (kg)"].get(), entries["📝 Piezīmes"].get()
)).pack(pady=10)

create_back_button(add_frame)

# ✏ Rediģēt treniņu
ttk.Label(edit_frame, text="✏ Rediģēt treniņu", font=("Arial", 16, "bold")).pack(pady=10)

# Listbox (saraksts) ar treniņiem
def update_training_list():
    all_trainings = view_trainings()  # Izsauc funkciju, lai iegūtu visus treniņus
    print("All Trainings:", all_trainings)  # Debugging to check what's returned

    if not all_trainings:  # If it's empty or None, handle it
        print("No trainings to display.")
        return  # Exit the function if there are no trainings

    training_list.delete(0, tk.END)  # Iztīra esošo sarakstu
    for index, training in enumerate(all_trainings):
        training_list.insert(tk.END, f"ID: {index + 1}, {training['datums']} - {training['vingrinājums']}")


training_list = tk.Listbox(edit_frame, width=50, height=10)
training_list.pack(pady=10)
update_training_list()

def on_select_training(event):
    selected_index = training_list.curselection()  # Atrod izvēlēto treniņu
    if selected_index:
        selected_index = selected_index[0]  # Paņem pirmo izvēlēto treniņu
        selected_training = view_trainings()[selected_index]  # Iegūst izvēlēto treniņu
        # Pievieno treniņa detaļas lauciņos
        entries["📅 Datums (YYYY-MM-DD)"].delete(0, tk.END)
        entries["📅 Datums (YYYY-MM-DD)"].insert(0, selected_training["datums"])
        entries["🏋 Vingrinājums"].delete(0, tk.END)
        entries["🏋 Vingrinājums"].insert(0, selected_training["vingrinājums"])
        entries["🔢 Komplekti"].delete(0, tk.END)
        entries["🔢 Komplekti"].insert(0, selected_training["komplekts"])
        entries["🔁 Atkārtojumi"].delete(0, tk.END)
        entries["🔁 Atkārtojumi"].insert(0, selected_training["atkārtojumi"])
        entries["🏋‍♂️ Svars (kg)"].delete(0, tk.END)
        entries["🏋‍♂️ Svars (kg)"].insert(0, selected_training["svars"])
        entries["📝 Piezīmes"].delete(0, tk.END)
        entries["📝 Piezīmes"].insert(0, selected_training["piezīmes"])

training_list.bind("<ButtonRelease-1>", on_select_training)  # Kvēlo treniņu izvēle

# Rediģēt treniņu pogas
def edit_selected_training():
    selected_index = training_list.curselection()
    if not selected_index:
        messagebox.showerror("Kļūda", "Lūdzu izvēlieties treniņu, kuru vēlaties rediģēt!")
        return

    selected_index = selected_index[0]
    selected_training = view_trainings()[selected_index]
    
    # Izsauc rediģēšanas funkciju   
    edit_training(
        selected_training["id"],  # Treniņa ID
        entries["📅 Datums (YYYY-MM-DD)"].get(),
        entries["🏋 Vingrinājums"].get(),
        entries["🔢 Komplekti"].get(),
        entries["🔁 Atkārtojumi"].get(),
        entries["🏋‍♂️ Svars (kg)"].get(),
        entries["📝 Piezīmes"].get()
    )

ttk.Button(edit_frame, text="✏ Rediģēt treniņu", command=edit_selected_training).pack(pady=10)

create_back_button(edit_frame)

# Rādīt sākuma rāmi
show_frame(home_frame)

window.mainloop()
