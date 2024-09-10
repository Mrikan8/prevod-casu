import tkinter as tk
from tkinter import messagebox

def calculate_time():
    try:
        s = int(entry.get())
        if s <= 0:
            messagebox.showerror(messages["error_title"], messages["error_message"])
            return
        
        unit = unit_var.get()
        if unit == messages["seconds"]:
            total_seconds = s
        elif unit == messages["minutes"]:
            total_seconds = s * 60
        elif unit == messages["hours"]:
            total_seconds = s * 3600
        else:
            messagebox.showerror(messages["error_title"], messages["invalid_unit"])
            return
        
        m = total_seconds // 60
        h = m // 60
        d = h // 24
        r = d // 365
        s = total_seconds % 60
        m = m % 60
        h = h % 24
        d = d % 365
        result_label.config(text=f"{messages['result']} {r} {messages['years']}, {d} {messages['days']}, {h} {messages['hours']}, {m} {messages['minutes']}, {s} {messages['seconds']}")
    except ValueError:
        messagebox.showerror(messages["error_title"], messages["invalid_input"])

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")
    entry.focus()

def set_language(lang):
    global messages
    if lang == "Čeština":
        messages = {
            "title": "Převod času",
            "prompt": "Zadej čas:",
            "convert": "Převést",
            "reset": "Znovu",
            "result": "výsledný čas je:",
            "years": "roků",
            "days": "D",
            "hours": "H",
            "minutes": "M",
            "seconds": "S",
            "error_title": "Chyba",
            "error_message": "asi to nepujde, znovu",
            "invalid_unit": "Neplatná jednotka",
            "invalid_input": "Prosím zadejte platný čas v sekundách"
        }
    elif lang == "English":
        messages = {
            "title": "Time Conversion",
            "prompt": "Enter time:",
            "convert": "Convert",
            "reset": "Reset",
            "result": "The resulting time is:",
            "years": "years",
            "days": "D",
            "hours": "H",
            "minutes": "M",
            "seconds": "S",
            "error_title": "Error",
            "error_message": "This won't work, try again",
            "invalid_unit": "Invalid unit",
            "invalid_input": "Please enter a valid time in seconds"
        }
    update_ui()

def update_ui():
    root.title(messages["title"])
    prompt_label.config(text=messages["prompt"])
    convert_button.config(text=messages["convert"])
    reset_button.config(text=messages["reset"])
    unit_menu["menu"].delete(0, "end")
    for unit in [messages["seconds"], messages["minutes"], messages["hours"]]:
        unit_menu["menu"].add_command(label=unit, command=lambda v=unit: unit_var.set(v))

# Vytvoření hlavního okna
root = tk.Tk()

# Výchozí jazyk
messages = {}

# Vytvoření a umístění widgetů
language_var = tk.StringVar(root)
language_var.set("Čeština")  # Výchozí hodnota
language_menu = tk.OptionMenu(root, language_var, "Čeština", "English", command=set_language)
language_menu.pack(pady=5)

prompt_label = tk.Label(root, text="")
prompt_label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)
entry.focus()

unit_var = tk.StringVar(root)
unit_var.set("seconds")  # Výchozí hodnota
unit_menu = tk.OptionMenu(root, unit_var, "seconds", "minutes", "hours")
unit_menu.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=calculate_time, width=20)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset, width=20)
reset_button.pack(pady=5)

# Nastavení výchozího jazyka
set_language("Čeština")

# Spuštění hlavní smyčky
root.mainloop()