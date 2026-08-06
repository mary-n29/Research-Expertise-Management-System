import tkinter as tk
from tkinter import ttk, messagebox

from db_connection import open_connection
from main_menu import open_main_menu


def connect_database():
    """Connect to the database and open the dashboard."""
    try:
        open_connection()

        status_label.config(
            text="● Connected",
            foreground="green"
        )

        messagebox.showinfo(
            "Success",
            "Connected to ResearchExpertiseDB."
        )

        root.withdraw()          # Hide the connection window
        open_main_menu(root)

    except Exception as e:
        status_label.config(
            text="● Not Connected",
            foreground="red"
        )

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# ---------------- Window ---------------- #

root = tk.Tk()
root.title("Research Expertise Management System")
root.geometry("900x650")
root.configure(bg="#F5F7FA")

style = ttk.Style()
style.theme_use("clam")

# ---------------- Header ---------------- #

header = tk.Frame(root, bg="#861F41", height=110)
header.pack(fill="x")

title = tk.Label(
    header,
    text="Research Expertise Management System",
    bg="#861F41",
    fg="white",
    font=("Segoe UI", 24, "bold")
)
title.pack(pady=(20, 5))

subtitle = tk.Label(
    header,
    text="Supporting Research Collaboration & Project Management",
    bg="#861F41",
    fg="white",
    font=("Segoe UI", 11)
)
subtitle.pack()

# ---------------- Connection Card ---------------- #

card = tk.Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)
card.pack(pady=50, padx=180, fill="both")

tk.Label(
    card,
    text="Database Connection",
    bg="white",
    fg="#2D3748",
    font=("Segoe UI", 16, "bold")
).pack(pady=20)

status_label = tk.Label(
    card,
    text="● Not Connected",
    bg="white",
    fg="red",
    font=("Segoe UI", 14, "bold")
)
status_label.pack()

ttk.Separator(card).pack(fill="x", padx=30, pady=20)

info = tk.Frame(card, bg="white")
info.pack()

tk.Label(info, text="Host:", bg="white", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w", padx=20)
tk.Label(info, text="localhost", bg="white").grid(row=0, column=1, sticky="w")

tk.Label(info, text="Database:", bg="white", font=("Segoe UI", 11, "bold")).grid(row=1, column=0, sticky="w", padx=20)
tk.Label(info, text="ResearchExpertiseDB", bg="white").grid(row=1, column=1, sticky="w")

tk.Label(info, text="DBMS:", bg="white", font=("Segoe UI", 11, "bold")).grid(row=2, column=0, sticky="w", padx=20)
tk.Label(info, text="MySQL 8.0", bg="white").grid(row=2, column=1, sticky="w")

# ---------------- Buttons ---------------- #

button_frame = tk.Frame(root, bg="#F5F7FA")
button_frame.pack(pady=20)

ttk.Button(
    button_frame,
    text="Connect to Database",
    command=connect_database
).grid(row=0, column=0, padx=15)

ttk.Button(
    button_frame,
    text="Exit",
    command=root.destroy
).grid(row=0, column=1)

# ---------------- Footer ---------------- #

footer = tk.Label(
    root,
    text="CS 5614 Database Project",
    bg="#F5F7FA",
    fg="gray"
)
footer.pack(side="bottom", pady=20)

root.mainloop()