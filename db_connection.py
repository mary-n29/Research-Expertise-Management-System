import tkinter as tk
from tkinter import messagebox
import mysql.connector


# ---------------------------------------------------------
# Database Connection
# ---------------------------------------------------------

connection = None


def open_connection():
    global connection

    try:
        # Avoid opening a second connection
        if connection is not None and connection.is_connected():
            return

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password_not_real",
            database="ResearchExpertiseDB"
        )

        if connection.is_connected():
            status_label.config(
                text="CONNECTED",
                fg="green"
            )

            detail_label.config(
                text="Connection to ResearchExpertiseDB established successfully."
            )

    except mysql.connector.Error as error:
        status_label.config(
            text="CONNECTION FAILED",
            fg="red"
        )

        detail_label.config(
            text="Unable to establish database connection."
        )

        messagebox.showerror(
            "Database Connection Error",
            str(error)
        )


def close_connection():
    global connection

    if connection is not None and connection.is_connected():
        connection.close()

    status_label.config(
        text="NOT CONNECTED",
        fg="red"
    )

    detail_label.config(
        text="No active database connection."
    )


# ---------------------------------------------------------
# Main Window
# ---------------------------------------------------------

root = tk.Tk()

root.title("CS 5614 - Database Connection")
root.geometry("600x550")
root.resizable(False, False)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

header_frame = tk.Frame(root)

header_frame.pack(
    fill="x",
    padx=30,
    pady=(25, 10)
)


project_title = tk.Label(
    header_frame,
    text="Research & Expertise Management System",
    font=("Arial", 17, "bold")
)

project_title.pack()


course_title = tk.Label(
    header_frame,
    text="CS 5614 - Database Project",
    font=("Arial", 11)
)

course_title.pack(pady=(5, 15))


separator = tk.Frame(
    root,
    height=2,
    bd=1,
    relief="sunken"
)

separator.pack(
    fill="x",
    padx=30
)


# ---------------------------------------------------------
# Connection Status
# ---------------------------------------------------------

connection_heading = tk.Label(
    root,
    text="Database Connection Status",
    font=("Arial", 13, "bold")
)

connection_heading.pack(pady=(25, 10))


status_label = tk.Label(
    root,
    text="NOT CONNECTED",
    font=("Arial", 18, "bold"),
    fg="red"
)

status_label.pack(pady=5)


detail_label = tk.Label(
    root,
    text="No active database connection.",
    font=("Arial", 10)
)

detail_label.pack(pady=(0, 20))


# ---------------------------------------------------------
# Database Information
# ---------------------------------------------------------

info_frame = tk.LabelFrame(
    root,
    text=" Database Information ",
    font=("Arial", 10, "bold"),
    padx=20,
    pady=12
)

info_frame.pack(
    fill="x",
    padx=80,
    pady=5
)


tk.Label(
    info_frame,
    text="DBMS:",
    font=("Arial", 10, "bold")
).grid(row=0, column=0, sticky="w", padx=10, pady=3)

tk.Label(
    info_frame,
    text="MySQL 8.0"
).grid(row=0, column=1, sticky="w", padx=10)


tk.Label(
    info_frame,
    text="Database:",
    font=("Arial", 10, "bold")
).grid(row=1, column=0, sticky="w", padx=10, pady=3)

tk.Label(
    info_frame,
    text="ResearchExpertiseDB"
).grid(row=1, column=1, sticky="w", padx=10)


tk.Label(
    info_frame,
    text="Host:",
    font=("Arial", 10, "bold")
).grid(row=2, column=0, sticky="w", padx=10, pady=3)

tk.Label(
    info_frame,
    text="localhost"
).grid(row=2, column=1, sticky="w", padx=10)


tk.Label(
    info_frame,
    text="Interface:",
    font=("Arial", 10, "bold")
).grid(row=3, column=0, sticky="w", padx=10, pady=3)

tk.Label(
    info_frame,
    text="Python"
).grid(row=3, column=1, sticky="w", padx=10)


# ---------------------------------------------------------
# Buttons
# ---------------------------------------------------------

button_frame = tk.Frame(root)

button_frame.pack(pady=25)


open_button = tk.Button(
    button_frame,
    text="Open Connection",
    width=18,
    command=open_connection
)

open_button.grid(
    row=0,
    column=0,
    padx=10
)


close_button = tk.Button(
    button_frame,
    text="Close Connection",
    width=18,
    command=close_connection
)

close_button.grid(
    row=0,
    column=1,
    padx=10
)


# ---------------------------------------------------------
# Start Application
# ---------------------------------------------------------

root.mainloop()