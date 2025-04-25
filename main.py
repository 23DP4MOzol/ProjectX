import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import add_training, view_trainings, edit_training, delete_training, show_statistics, search_trainings, get_recommendation
from datetime import datetime, timedelta
import numpy as np

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

# Funkcija, kas tiks izsaukta, kad lietotājs izvēlēsies treniņu no saraksta
def on_select_edit_training(event):
    selected_index = edit_training_list.curselection()  # Atrod izvēlēto treniņu
    if selected_index:
        selected_index = selected_index[0]
        selected_training = view_trainings()[selected_index]  # Skatāmies treniņus
        open_edit_window(selected_training)  # Atveram rediģēšanas logu

# Izveido sarakstu ar treniņiem
edit_training_list = tk.Listbox(edit_frame, width=50, height=10)
edit_training_list.pack(pady=10)

# Funkcija, kas atjauno sarakstu un pievieno jaunas vērtības
def update_edit_training_list():
    all_trainings = view_trainings()
    edit_training_list.delete(0, tk.END)
    for index, training in enumerate(all_trainings):
        edit_training_list.insert(tk.END, f"ID: {training['id']}, {training['datums']} - {training['vingrinājums']}")

# Pievienot notikumu: dubultklikšķis uz treniņa saraksta
edit_training_list.bind("<Double-1>", on_select_edit_training)
update_edit_training_list()

# Atpakaļ poga galvenajā rediģēšanas rāmī
def create_back_button(frame):
    ttk.Button(frame, text="⬅ Atpakaļ", command=lambda: show_frame(home_frame), width=15).pack(pady=10)

create_back_button(edit_frame)  # Šeit pievienojam atpakaļ pogu rediģēšanas rāmim


# Funkcija, lai atvērtu rediģēšanas logu
def open_edit_window(training):
    # Izveido jaunu top-level logu
    edit_window = tk.Toplevel()
    edit_window.title(f"Rediģēt treniņu: {training['datums']} - {training['vingrinājums']}")

    # Dizains
    edit_frame = ttk.Frame(edit_window, padding=20)
    edit_frame.grid(row=0, column=0)

    # Etiķetes un lauki
    labels = ["Datums", "Vingrinājums", "Komplekts", "Atkārtojumi", "Svars", "Piezīmes"]
    keys = ["datums", "vingrinājums", "komplekts", "atkārtojumi", "svars", "piezīmes"]
    entries = {}

    for i, (label, key) in enumerate(zip(labels, keys)):
        tk.Label(edit_frame, text=label, font=("Arial", 12)).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entry = ttk.Entry(edit_frame, width=30)
        entry.insert(0, training[key])  # Ieliek esošo vērtību
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries[key] = entry  # Saglabājam laukus, lai vēlāk piekļūtu tiem

    # Funkcija, lai saglabātu izmaiņas
    def save_changes():
        updated_values = {key: entries[key].get() for key in keys}
        print("Saglabātie dati:", updated_values)  # Izdrukājam saglabātos datus
        # Nododam visus atjauninātos datus uz edit_training funkciju
        edit_training(training["id"], **updated_values)  # Saglabājam izmaiņas treniņā
        update_edit_training_list()  # Atjaunojam sarakstu
        messagebox.showinfo("Veiksmīgi", "Treniņš veiksmīgi rediģēts!")  # Paziņojums, ka izmaiņas saglabātas
        edit_window.destroy()  # Aizveram logu


    # Poga, kas saglabā izmaiņas
    save_button = ttk.Button(edit_frame, text="Saglabāt izmaiņas", command=save_changes)
    save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    # Poga "Atpakaļ"
    back_button = ttk.Button(edit_frame, text="Atpakaļ", command=edit_window.destroy, width=15)
    back_button.grid(row=len(labels) + 1, column=0, columnspan=2, pady=10)





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

# Saglabāsim šķirošanas secību
sort_order = "desc"  # "desc" nozīmē no jaunākā uz vecāko, "asc" - otrādi
alphabetical_order = "asc"  # "asc" nozīmē no A-Z, "desc" - Z-A

# Funkcija, kas atjauno sarakstu un šķiro to pēc datuma
def update_view_trainings():
    all_trainings = view_trainings()  # Šeit jābūt tavai funkcijai, kas iegūst visus treniņus

    # Atkarībā no šķirošanas secības, šķirojam treniņus
    if sort_order == "desc":
        sorted_trainings = sorted(all_trainings, key=lambda x: x['datums'], reverse=True)
    else:
        sorted_trainings = sorted(all_trainings, key=lambda x: x['datums'])

    # Ievieto treniņus sarakstā
    view_list.delete(0, tk.END)
    for training in sorted_trainings:
        view_list.insert(tk.END, f"{training['datums']} - {training['vingrinājums']}")

# Funkcija, kas pārslēdz šķirošanas secību pēc nosaukuma (A-Z/Z-A)
def toggle_alphabetical_order():
    global alphabetical_order
    # Mainām šķirošanas secību
    if alphabetical_order == "asc":
        alphabetical_order = "desc"
        alphabetical_sort_button.config(text="📚 Sortēt no Z-A")  # Mainām pogas tekstu
    else:
        alphabetical_order = "asc"
        alphabetical_sort_button.config(text="📚 Sortēt no A-Z")  # Mainām pogas tekstu
    
    # Atjaunojam treniņu sarakstu pēc jaunā secības
    update_alphabetical_sort()

# Funkcija, kas atjauno sarakstu un šķiro to pēc nosaukuma
def update_alphabetical_sort():
    all_trainings = view_trainings()  # Šeit jābūt tavai funkcijai, kas iegūst visus treniņus

    # Atkarībā no šķirošanas secības, šķirojam treniņus pēc nosaukuma
    if alphabetical_order == "desc":
        sorted_trainings = sorted(all_trainings, key=lambda x: x['vingrinājums'], reverse=True)
    else:
        sorted_trainings = sorted(all_trainings, key=lambda x: x['vingrinājums'])

    # Ievieto treniņus sarakstā
    view_list.delete(0, tk.END)
    for training in sorted_trainings:
        view_list.insert(tk.END, f"{training['datums']} - {training['vingrinājums']}")

# Funkcija, kas pārslēdz šķirošanas secību pēc datuma (asc/desc)
def toggle_sort_order():
    global sort_order
    # Mainām šķirošanas secību
    if sort_order == "desc":
        sort_order = "asc"
    else:
        sort_order = "desc"
    
    # Atjaunojam treniņu sarakstu pēc jaunā secības
    update_view_trainings()

# Izveido treniņu sarakstu
view_list = tk.Listbox(view_frame, width=50, height=10)
view_list.pack(pady=10)

# Izveido pogu "Sortēt pēc datuma"
date_sort_button = ttk.Button(view_frame, text="📅 Sortēt pēc datuma", command=toggle_sort_order)
date_sort_button.pack(pady=5)

# Izveido pogu "Sortēt pēc nosaukuma A-Z/Z-A"
alphabetical_sort_button = ttk.Button(view_frame, text="📚 Sortē no A-Z", command=toggle_alphabetical_order)
alphabetical_sort_button.pack(pady=5)

# Atjaunojam sarakstu sākotnēji
update_view_trainings()

# Izveido atpakaļ pogu
create_back_button(view_frame)


# Funkcija, kas tiek izsaukta, kad tiek izvēlēts treniņš no saraksta
def on_select_view_training(event):
    selected_index = view_list.curselection()  # Atrod izvēlēto treniņu
    if selected_index:
        selected_index = selected_index[0]
        selected_training = view_trainings()[selected_index]  # Skatāmies treniņus
        show_training_details(selected_training)  # Parādām treniņa detaļas

# Funkcija, lai parādītu treniņa informāciju
def show_training_details(training):
    details_window = tk.Toplevel(window)
    details_window.title(f"Treniņš: {training['datums']} - {training['vingrinājums']}")

    # Pievienojam treniņa informāciju
    details_label = f"Datums: {training['datums']}\n"
    details_label += f"Vingrinājums: {training['vingrinājums']}\n"
    details_label += f"Komplekts: {training['komplekts']}\n"
    details_label += f"Atkārtojumi: {training['atkārtojumi']}\n"
    details_label += f"Svars: {training['svars']} kg\n"
    details_label += f"Piezīmes: {training['piezīmes']}"

    ttk.Label(details_window, text=details_label, font=("Arial", 12)).pack(pady=20)

    # Poga aizvērt logu
    ttk.Button(details_window, text="Aizvērt", command=details_window.destroy).pack(pady=10)

# Atjauninām sarakstu, lai parādītu treniņus un pievienojam notikumu, lai varētu izvēlēties treniņu
view_list.bind("<Double-1>", on_select_view_training)


## Statistika



def create_new_window(title, fig):
    # Izveidojam jaunu logu
    new_window = tk.Toplevel()
    new_window.title(title)
    
    # Zīmējam matplotlib diagrammu jaunajā logā
    canvas = FigureCanvasTkAgg(fig, master=new_window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)
    
    # Poga, lai aizvērtu logu
    ttk.Button(new_window, text="Aizvērt", command=new_window.destroy).pack(pady=10)


ttk.Label(stats_frame, text="📊 Statistika", font=("Arial", 16, "bold")).pack(pady=10)

# Funkcijas, kas tiks izsauktas, kad tiek nospiestas pogas
def show_monthly_chart():
    # Iegūstam visus treniņus
    all_trainings = view_trainings()
    
    # Sagatavojam datus mēneša analīzei
    months = []
    training_count = {}

    for training in all_trainings:
        # Iegūstam mēnesi no datuma
        date = datetime.strptime(training['datums'], "%Y-%m-%d")
        month_year = date.strftime("%Y-%m")  # Piemēram, "2023-04"
        
        if month_year not in months:
            months.append(month_year)
            training_count[month_year] = 0
        training_count[month_year] += 1

    # Sagatavojam datus diagrammai
    sorted_months = sorted(training_count.keys())
    counts = [training_count[month] for month in sorted_months]

    # Zīmējam diagrammu
    fig, ax = plt.subplots()
    ax.bar(sorted_months, counts, color='skyblue')
    ax.set_title("Treniņu skaits pa mēnešiem")
    ax.set_xlabel("Mēnesis")
    ax.set_ylabel("Treniņu skaits")
    ax.tick_params(axis='x', rotation=45)

    # Atveram diagrammu jaunā logā
    create_new_window("Mēneša Diagramma", fig)


def show_weekly_chart():
    # Iegūstam visus treniņus
    all_trainings = view_trainings()

    # Sagatavojam datus nedēļas analīzei
    weeks = []
    training_count = {}

    for training in all_trainings:
        # Iegūstam datumu un pārveidojam uz nedēļu (nedēļas sākums)
        date = datetime.strptime(training['datums'], "%Y-%m-%d")
        week_start = date - timedelta(days=date.weekday())  # Nedēļas sākums (pirmdiena)
        week_str = week_start.strftime("%Y-%m-%d")  # Piemēram, "2023-04-03" (pirmdiena)
        
        if week_str not in weeks:
            weeks.append(week_str)
            training_count[week_str] = 0
        training_count[week_str] += 1

    # Sagatavojam datus diagrammai
    sorted_weeks = sorted(training_count.keys())
    counts = [training_count[week] for week in sorted_weeks]

    # Zīmējam diagrammu
    fig, ax = plt.subplots()
    ax.bar(sorted_weeks, counts, color='lightcoral')
    ax.set_title("Treniņu skaits pa nedēļām")
    ax.set_xlabel("Nedēļa (pirmdiena)")
    ax.set_ylabel("Treniņu skaits")
    ax.tick_params(axis='x', rotation=45)

    # Atveram diagrammu jaunā logā
    create_new_window("Nedēļas Diagramma", fig)


def show_general_chart_by_weight():
    # Iegūstam visus treniņus
    all_trainings = view_trainings()

    # Sagatavojam datus pēc svara
    weight_count = {}

    for training in all_trainings:
        # Iegūstam svaru no treniņa
        weight = training.get('svars')
        
        if weight is None:
            continue  # Ja svara nav, tad izlaidīsim šo ierakstu

        # Skaitām, cik reizes katrs svars parādās
        if weight not in weight_count:
            weight_count[weight] = 0
        weight_count[weight] += 1

    # Sagatavojam datus diagrammai
    weights = list(weight_count.keys())
    counts = list(weight_count.values())

    # Zīmējam diagrammu
    fig, ax = plt.subplots()
    ax.bar(weights, counts, color='lightblue')
    ax.set_title("Treniņu skaits pēc svara")
    ax.set_xlabel("Svars (kg)")
    ax.set_ylabel("Treniņu skaits")
    ax.tick_params(axis='x', rotation=45)

    # Atveram diagrammu jaunā logā
    create_new_window("Vispārējā Diagramma pēc Svara", fig)

def categorize_weights(weight):
    if weight < 50:
        return "<50 kg"
    elif weight < 70:
        return "50-70 kg"
    elif weight < 90:
        return "70-90 kg"
    else:
        return "90+ kg"


def show_stats():
    show_statistics()  # Parādām statistiku

# Poga Mēneša diagramma
ttk.Button(stats_frame, text="📊 Mēneša Diagramma", command=show_monthly_chart).pack(pady=5)

# Poga Nedēļas diagramma
ttk.Button(stats_frame, text="📊 Nedēļas Diagramma", command=show_weekly_chart).pack(pady=5)

# Poga Vispārējā diagramma pēc svara
ttk.Button(stats_frame, text="📊 Vispārējā Diagramma pēc Svara", command=show_general_chart_by_weight).pack(pady=5)

# Poga Skatīt statistiku
ttk.Button(stats_frame, text="📊 Skatīt statistiku", command=show_stats).pack(pady=5)

create_back_button(stats_frame)  # Atpakaļ poga


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
