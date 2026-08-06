import tkinter as tk
from tkinter import ttk

from tkinter import messagebox

from db_connection import open_connection
from load_researcher import load_researchers
from statistics_window import open_statistics_window

def open_researcher_window():

    window = tk.Toplevel()

    window.title("Researcher Management")
    window.geometry("1000x700")
    window.configure(bg="#F5F7FA")

    # ================= HEADER =================

    header = tk.Frame(window, bg="#861F41", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="Researcher Management",
        bg="#861F41",
        fg="white",
        font=("Segoe UI", 20, "bold")
    ).pack(pady=(20,5))

    tk.Label(
        header,
        text="Add, Update and Delete Researchers",
        bg="#861F41",
        fg="white",
        font=("Segoe UI",10)
    ).pack()

    # ================= MAIN CONTENT =================

    content = tk.Frame(window, bg="#F5F7FA")
    content.pack(fill="both", expand=True, padx=20, pady=20)

    # ---------- LEFT SIDE (FORM) ----------

    form = tk.LabelFrame(
        content,
        text=" Researcher Information ",
        font=("Segoe UI",11,"bold"),
        padx=15,
        pady=15,
        bg="white"
    )

    form.pack(side="left", fill="y")

    labels = [
        "Researcher ID",
        "First Name",
        "Last Name",
        "Department",
        "Position"
    ]

    entries = {}

    for i, label in enumerate(labels):

        tk.Label(
            form,
            text=label,
            bg="white",
            font=("Segoe UI",10)
        ).grid(row=i, column=0, sticky="w", pady=8)

        entry = ttk.Entry(form, width=30)

        entry.grid(row=i, column=1, pady=8)

        entries[label] = entry

    # ---------- BUTTONS ----------

    button_frame = tk.Frame(form, bg="white")
    button_frame.grid(row=6, column=0, columnspan=2, pady=20)

    tk.Button(
        button_frame,
        text="Add",
        bg="#2E8B57",
        fg="white",
        width=12,
        command=lambda: add_researcher(entries, tree)
        ).grid(row=0,column=0,padx=5)

    tk.Button(
        button_frame,
        text="Update",
        bg="#E87722",
        fg="white",
        width=12,
        command=lambda: update_researcher(entries, tree)
        ).grid(row=0,column=1,padx=5)

    tk.Button(
        button_frame,
        text="Delete",
        bg="#C0392B",
        fg="white",
        width=12,
        command=lambda: delete_researcher(entries, tree)
        ).grid(row=0,column=2,padx=5)

    tk.Button(
        button_frame,
        text="View Statistics",
        bg="#2C7BE5",
        fg="white",
        width=14,
        command=open_statistics_window
        ).grid(row=0,column=3,padx=5)

    # ---------- RIGHT SIDE (TABLE) ----------

    table_frame = tk.LabelFrame(
        content,
        text=" Existing Researchers ",
        font=("Segoe UI",11,"bold"),
        padx=10,
        pady=10,
        bg="white"
    )

    table_frame.pack(side="right", fill="both", expand=True, padx=(20,0))

    columns = (
        "ID",
        "First Name",
        "Last Name",
        "Department",
        "Position"
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    tree.pack(fill="both", expand=True)
    load_researchers(tree)

    tree.bind(
        "<<TreeviewSelect>>",
        lambda event: populate_form(tree, entries)
    )

    ttk.Button(
        window,
        text="Back",
        command=window.destroy
    ).pack(pady=10)

def populate_form(tree, entries):
    """Fill the form fields with the values of the row selected in the table."""

    selected = tree.selection()

    if not selected:
        return

    values = tree.item(selected[0], "values")

    fields = [
        "Researcher ID",
        "First Name",
        "Last Name",
        "Department",
        "Position"
    ]

    for field, value in zip(fields, values):
        entries[field].delete(0, tk.END)
        entries[field].insert(0, value)


def update_researcher(entries, tree):

    try:
        researcher_id = entries["Researcher ID"].get().strip()

        values = (
            entries["First Name"].get().strip(),
            entries["Last Name"].get().strip(),
            entries["Department"].get().strip(),
            entries["Position"].get().strip(),
            researcher_id
        )

        if researcher_id == "" or any(value == "" for value in values[:-1]):
            messagebox.showwarning(
                "Missing Information",
                "Please select a researcher and complete all fields."
            )
            return

        conn = open_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE RESEARCHER
        SET FName = %s,
            LName = %s,
            Department = %s,
            Position = %s
        WHERE ResearcherID = %s
        """

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showwarning(
                "Not Found",
                f"No researcher found with ID {researcher_id}."
            )
        else:
            load_researchers(tree)
            for entry in entries.values():
                entry.delete(0, tk.END)

            messagebox.showinfo(
                "Success",
                "Researcher updated successfully!"
            )

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


def delete_researcher(entries, tree):

    try:
        researcher_id = entries["Researcher ID"].get().strip()

        if researcher_id == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select a researcher to delete."
            )
            return

        conn = open_connection()
        cursor = conn.cursor()

        # Check how many dependent rows exist across the tables that
        # reference RESEARCHER
        cursor.execute(
            "SELECT COUNT(*) FROM PROJECT_MEMBERSHIP WHERE ResearcherID = %s",
            (researcher_id,)
        )
        membership_count = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM RESEARCHER_SKILL WHERE ResearcherID = %s",
            (researcher_id,)
        )
        skill_count = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM PUBLICATION_AUTHOR WHERE ResearcherID = %s",
            (researcher_id,)
        )
        author_count = cursor.fetchone()[0]

        if membership_count > 0 or skill_count > 0 or author_count > 0:
            warning = (
                f"Researcher ID {researcher_id} has {membership_count} "
                f"project membership(s), {skill_count} skill record(s), "
                f"and {author_count} publication authorship(s) linked to them.\n\n"
                f"Deleting this researcher will also remove those records. "
                f"This cannot be undone. Continue?"
            )
        else:
            warning = f"Are you sure you want to delete researcher ID {researcher_id}?"

        confirm = messagebox.askyesno("Confirm Delete", warning)

        if not confirm:
            return

        # Remove dependent rows first, then the researcher itself
        cursor.execute(
            "DELETE FROM PROJECT_MEMBERSHIP WHERE ResearcherID = %s",
            (researcher_id,)
        )
        cursor.execute(
            "DELETE FROM RESEARCHER_SKILL WHERE ResearcherID = %s",
            (researcher_id,)
        )
        cursor.execute(
            "DELETE FROM PUBLICATION_AUTHOR WHERE ResearcherID = %s",
            (researcher_id,)
        )
        cursor.execute(
            "DELETE FROM RESEARCHER WHERE ResearcherID = %s",
            (researcher_id,)
        )
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showwarning(
                "Not Found",
                f"No researcher found with ID {researcher_id}."
            )
        else:
            load_researchers(tree)
            for entry in entries.values():
                entry.delete(0, tk.END)

            messagebox.showinfo(
                "Success",
                "Researcher deleted successfully!"
            )

    except Exception as e:
        conn.rollback()
        messagebox.showerror(
            "Database Error",
            str(e)
        )


def add_researcher(entries, tree):
    
    try:
        conn = open_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO RESEARCHER
        (ResearcherID, FName, LName, Department, Position)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            int(entries["Researcher ID"].get().strip()),
            entries["First Name"].get().strip(),
            entries["Last Name"].get().strip(),
            entries["Department"].get().strip(),
            entries["Position"].get().strip()
        )


        if any(value == "" for value in values):
            messagebox.showwarning(
                "Missing Information",
                "Please complete all fields."
            )
            return

        cursor.execute(sql, values)

        conn.commit()
        load_researchers(tree)
        for entry in entries.values():
            entry.delete(0, tk.END)

        messagebox.showinfo(
            "Success",
            "Researcher added successfully!"
        )

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )