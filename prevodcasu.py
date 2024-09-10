import tkinter as tk
from tkinter import messagebox

def calculate_time():
    try:
        s = int(entry.get())
        if s <= 0:
            messagebox.showerror("Chyba", "asi to nepujde, znovu")
            return
        
        unit = unit_var.get()
        if unit == "Sekundy":
            total_seconds = s
        elif unit == "Minuty":
            total_seconds = s * 60
        elif unit == "Hodiny":
            total_seconds = s * 3600
        else:
            messagebox.showerror("Chyba", "Neplatná jednotka")
            return
        
        m = total_seconds // 60
        h = m // 60
        d = h // 24
        r = d // 365
        s = total_seconds % 60
        m = m % 60
        h = h % 24
        d = d % 365
        result_label.config(text=f"výsledný čas je: {r} roků, {d} D, {h} H, {m} M, {s} S")
    except ValueError:
        messagebox.showerror("Chyba", "Prosím zadejte platný čas v sekundách")

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")
    entry.focus()

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Převod času")

# Vytvoření a umístění widgetů
tk.Label(root, text="Zadej čas:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
entry.focus()

unit_var = tk.StringVar(root)
unit_var.set("Sekundy")  # Výchozí hodnota
unit_menu = tk.OptionMenu(root, unit_var, "Sekundy", "Minuty", "Hodiny")
unit_menu.pack(pady=5)

tk.Button(root, text="Převést", command=calculate_time, width=20).pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

tk.Button(root, text="Znovu", command=reset, width=20).pack(pady=5)

# Spuštění hlavní smyčky
root.mainloop()