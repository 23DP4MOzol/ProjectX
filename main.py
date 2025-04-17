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
    {
        "datums": entries["📅 Datums (YYYY-MM-DD)"].get(),
        "vingrinājums": entries["🏋 Vingrinājums"].get(),
        "komplekts": entries["🔢 Komplekti"].get(),
        "atkārtojumi": entries["🔁 Atkārtojumi"].get(),
        "svars": entries["🏋‍♂️ Svars (kg)"].get(),
        "piezīmes": entries["📝 Piezīmes"].get()
    }
)).pack(pady=10)

create_back_button(add_frame)

# ✏ Rediģēt treniņu
ttk.Label(edit_frame, text="✏ Rediģēt treniņu", font=("Arial", 16, "bold")).pack(pady=10)

edit_training_list = tk.Listbox(edit_frame, width=50, height=10)
edit_training_list.pack(pady=10)

def update_edit_training_list():
    all_trainings = view_trainings()
    edit_training_list.delete(0, tk.END)
    for index, training in enumerate(all_trainings):
        edit_training_list.insert(tk.END, f"ID: {index + 1}, {training['datums']} - {training['vingrinājums']}")

def on_select_edit_training(event):
    selected_index = edit_training_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        selected_training = view_trainings()[selected_index]
        open_edit_window(selected_training)


edit_training_list.bind("<Double-Button-1>", on_select_edit_training)


update_edit_training_list()


def edit_selected_training():
    selected_index = edit_training_list.curselection()
    if not selected_index:
        messagebox.showerror("Kļūda", "Lūdzu izvēlieties treniņu, kuru vēlaties rediģēt!")
        return
    selected_index = selected_index[0]
    selected_training = view_trainings()[selected_index]
    edit_training(
        selected_training["id"],
        entries["📅 Datums (YYYY-MM-DD)"].get(),
        entries["🏋 Vingrinājums"].get(),
        entries["🔢 Komplekti"].get(),
        entries["🔁 Atkārtojumi"].get(),
        entries["🏋‍♂️ Svars (kg)"].get(),
        entries["📝 Piezīmes"].get()
    )
    update_edit_training_list()


ttk.Button(edit_frame, text="✏ Rediģēt treniņu", command=edit_selected_training).pack(pady=10)
create_back_button(edit_frame)

def open_edit_window(training):
    edit_window = tk.Toplevel()
    edit_window.title("Rediģēt treniņu")

    # Labels + Entry fields
    labels = ["Datums", "Vingrinājums", "Komplekts", "Atkārtojumi", "Svars", "Piezīmes"]
    keys = ["datums", "vingrinājums", "komplekts", "atkārtojumi", "svars", "piezīmes"]
    entries = {}

    for i, (label, key) in enumerate(zip(labels, keys)):
        tk.Label(edit_window, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entry = tk.Entry(edit_window, width=30)
        entry.insert(0, training.get(key, ""))
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries[key] = entry

    # Saglabāšanas poga
    def save_changes():
        updated_values = {key: entries[key].get() for key in keys}
        edit_training(
            training_id=training["id"],
            datums=updated_values["datums"],
            vingrinajums=updated_values["vingrinājums"],
            komplekts=updated_values["komplekts"],
            atkārtojumi=updated_values["atkārtojumi"],
            svars=updated_values["svars"],
            piezīmes=updated_values["piezīmes"]
        )
        edit_window.destroy()

    tk.Button(edit_window, text="Saglabāt izmaiņas", command=save_changes).grid(row=len(labels), column=0, columnspan=2, pady=10)


# 🗑 Dzēst treniņu
ttk.Label(delete_frame, text="🗑 Dzēst treniņu", font=("Arial", 16, "bold")).pack(pady=10)

def update_training_list_for_deletion():
    all_trainings = view_trainings()

    # Pārbaudīt, vai ir kādi treniņi
    if not all_trainings:
        messagebox.showinfo("Treniņi", "Nav pieejami treniņi.")
        return

    # Tīrām iepriekšējos datus no saraksta
    training_list.delete(0, tk.END)

    for index, training in enumerate(all_trainings):
        # Pieejamās atslēgas no JSON
        date = training.get('datums', 'Nav datuma')
        training_type = training.get('vingrinājums', 'Nav vingrinājuma')
        sets = training.get('komplekts', 'Nav komplektu')
        repetitions = training.get('atkārtojumi', 'Nav atkārtojumu')
        weight = training.get('svars', 'Nav svara')
        notes = training.get('piezīmes', 'Nav piezīmju')

        # Ievietojam treniņu sarakstā
        training_list.insert(tk.END, f"ID: {index + 1}, {date} - {training_type}, {sets} komplekti, {repetitions} atkārtojumi, {weight} kg, {notes}")

def delete_selected_training():
    selected_index = training_list.curselection()
    if not selected_index:
        messagebox.showerror("Kļūda", "Lūdzu izvēlieties treniņu, kuru vēlaties dzēst!")
        return
    selected_index = selected_index[0]
    selected_training = view_trainings()[selected_index]
    confirm = messagebox.askyesno("Apstiprinājums", f"Vai tiešām vēlaties dzēst treniņu: {selected_training['datums']} - {selected_training['vingrinājums']}?")
    if confirm:
        delete_training(selected_training["id"])
        update_training_list_for_deletion()

training_list = tk.Listbox(delete_frame, width=50, height=10)
training_list.pack(pady=10)

update_training_list_for_deletion()

ttk.Button(delete_frame, text="🗑 Dzēst treniņu", command=delete_selected_training).pack(pady=10)
create_back_button(delete_frame)

# Skatīt treniņus
ttk.Label(view_frame, text="📅 Skatīt treniņus", font=("Arial", 16, "bold")).pack(pady=10)

def update_view_trainings():
    all_trainings = view_trainings()
    view_list.delete(0, tk.END)
    for training in all_trainings:
        view_list.insert(tk.END, f"{training['datums']} - {training['vingrinājums']}")

view_list = tk.Listbox(view_frame, width=50, height=10)
view_list.pack(pady=10)
update_view_trainings()

create_back_button(view_frame)

# Statistika
ttk.Label(stats_frame, text="📊 Statistika", font=("Arial", 16, "bold")).pack(pady=10)

def show_stats():
    show_statistics()

ttk.Button(stats_frame, text="📊 Skatīt statistiku", command=show_stats).pack(pady=10)
create_back_button(stats_frame)

# Meklēšana
ttk.Label(search_frame, text="🔍 Meklēt treniņus pēc datuma(YYYY-MM-DD)", font=("Arial", 16, "bold")).pack(pady=10)

def search_training():
    date = search_entry.get()
    search_trainings(date)

search_entry = ttk.Entry(search_frame, width=30)
search_entry.pack(pady=10)

ttk.Button(search_frame, text="🔍 Meklēt", command=search_training).pack(pady=10)
create_back_button(search_frame)

# Ieteikumi
ttk.Label(recommend_frame, text="💡 Ieteikums nākamajam treniņam", font=("Arial", 16, "bold")).pack(pady=10)

def recommend_training():
    get_recommendation()

ttk.Button(recommend_frame, text="💡 Ieteikums", command=recommend_training).pack(pady=10)
create_back_button(recommend_frame)

# Sākuma rāmis
show_frame(home_frame)

window.mainloop()
