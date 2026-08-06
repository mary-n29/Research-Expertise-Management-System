import tkinter as tk
from tkinter import ttk

from researcher import open_researcher_window
from project import open_project_window
from publication import open_publication_window


def open_main_menu(parent):

    menu = tk.Toplevel(parent)
    menu.title("Main Dashboard")
    menu.geometry("950x700")
    menu.configure(bg="#F5F7FA")

    # ---------- Header ----------

    header = tk.Frame(menu, bg="#861F41", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="Research Expertise Management System",
        bg="#861F41",
        fg="white",
        font=("Segoe UI", 22, "bold")
    ).pack(pady=(15, 5))

    tk.Label(
        header,
        text="Welcome! Select a module below.",
        bg="#861F41",
        fg="white",
        font=("Segoe UI", 11)
    ).pack()

    # ---------- Content ----------

    content = tk.Frame(menu, bg="#F5F7FA")
    content.pack(expand=True)

    researcher_btn = tk.Button(
        content,
        text="👤\n\nResearchers\n\nManage Researchers",
        width=22,
        height=8,
        bg="white",
        font=("Segoe UI", 11, "bold"),
        command=open_researcher_window,
        cursor="hand2"
    )

    project_btn = tk.Button(
        content,
        text="📁\n\nProjects\n\nManage Projects",
        width=22,
        height=8,
        bg="white",
        font=("Segoe UI", 11, "bold"),
        command=open_project_window,
        cursor="hand2"
    )

    publication_btn = tk.Button(
        content,
        text="📄\n\nPublications\n\nManage Publications",
        width=22,
        height=8,
        bg="white",
        font=("Segoe UI", 11, "bold"),
        command=open_publication_window,
        cursor="hand2"
    )

    researcher_btn.grid(row=0, column=0, padx=25, pady=25)

    project_btn.grid(row=0, column=1, padx=25, pady=25)

    publication_btn.grid(row=1, column=0, padx=25, pady=25)

    ttk.Button(
        menu,
        text="Exit",
        command=parent.destroy
    ).pack(pady=20)