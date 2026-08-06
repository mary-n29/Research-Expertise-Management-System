import tkinter as tk
from tkinter import ttk, messagebox

from db_connection import open_connection


def open_statistics_window():
    """Open a window showing aggregate statistics about researchers."""

    window = tk.Toplevel()
    window.title("Researcher Statistics")
    window.geometry("700x600")
    window.configure(bg="#F5F7FA")

    # ================= HEADER =================

    header = tk.Frame(window, bg="#861F41", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="Researcher Statistics",
        bg="#861F41",
        fg="white",
        font=("Segoe UI", 20, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        header,
        text="Aggregate Summary of Researcher Data",
        bg="#861F41",
        fg="white",
        font=("Segoe UI", 10)
    ).pack()

    content = tk.Frame(window, bg="#F5F7FA")
    content.pack(fill="both", expand=True, padx=20, pady=20)

    try:
        conn = open_connection()
        cursor = conn.cursor()

        # ---- Aggregate 1: total number of researchers (COUNT) ----
        cursor.execute("SELECT COUNT(*) FROM RESEARCHER")
        total_count = cursor.fetchone()[0]

        # ---- Aggregate 2: researchers per department (COUNT + GROUP BY) ----
        cursor.execute("""
            SELECT Department, COUNT(*) AS NumResearchers
            FROM RESEARCHER
            GROUP BY Department
            ORDER BY NumResearchers DESC
        """)
        by_department = cursor.fetchall()

        # ---- Aggregate 3: researchers per position (COUNT + GROUP BY) ----
        cursor.execute("""
            SELECT Position, COUNT(*) AS NumResearchers
            FROM RESEARCHER
            GROUP BY Position
            ORDER BY NumResearchers DESC
        """)
        by_position = cursor.fetchall()

        # ---- Bonus aggregate: MIN / MAX ResearcherID ----
        cursor.execute("SELECT MIN(ResearcherID), MAX(ResearcherID) FROM RESEARCHER")
        min_id, max_id = cursor.fetchone()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        window.destroy()
        return

    # ---------- Total Researchers ----------

    total_frame = tk.LabelFrame(
        content,
        text=" Total Researchers (COUNT) ",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        padx=15,
        pady=15
    )
    total_frame.pack(fill="x", pady=(0, 15))

    tk.Label(
        total_frame,
        text=str(total_count),
        bg="white",
        fg="#861F41",
        font=("Segoe UI", 22, "bold")
    ).pack()

    tk.Label(
        total_frame,
        text=f"Researcher ID range: {min_id} \u2013 {max_id}  (MIN / MAX)",
        bg="white",
        fg="#555555",
        font=("Segoe UI", 9)
    ).pack(pady=(5, 0))

    # ---------- By Department ----------

    dept_frame = tk.LabelFrame(
        content,
        text=" Researchers by Department (COUNT + GROUP BY) ",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        padx=10,
        pady=10
    )
    dept_frame.pack(fill="both", expand=True, pady=(0, 15))

    dept_tree = ttk.Treeview(
        dept_frame,
        columns=("Department", "Count"),
        show="headings",
        height=5
    )
    dept_tree.heading("Department", text="Department")
    dept_tree.heading("Count", text="Number of Researchers")
    dept_tree.column("Department", anchor="w")
    dept_tree.column("Count", anchor="center")
    dept_tree.pack(fill="both", expand=True)

    for dept, count in by_department:
        dept_tree.insert("", tk.END, values=(dept, count))

    # ---------- By Position ----------

    pos_frame = tk.LabelFrame(
        content,
        text=" Researchers by Position (COUNT + GROUP BY) ",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        padx=10,
        pady=10
    )
    pos_frame.pack(fill="both", expand=True)

    pos_tree = ttk.Treeview(
        pos_frame,
        columns=("Position", "Count"),
        show="headings",
        height=5
    )
    pos_tree.heading("Position", text="Position")
    pos_tree.heading("Count", text="Number of Researchers")
    pos_tree.column("Position", anchor="w")
    pos_tree.column("Count", anchor="center")
    pos_tree.pack(fill="both", expand=True)

    for pos, count in by_position:
        pos_tree.insert("", tk.END, values=(pos, count))

    # ---------- Close ----------

    ttk.Button(
        window,
        text="Close",
        command=window.destroy
    ).pack(pady=15)