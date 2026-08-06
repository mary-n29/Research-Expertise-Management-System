import tkinter as tk
from tkinter import ttk

from tkinter import messagebox

from db_connection import open_connection
from load_project import load_projects


def open_project_window():

    window = tk.Toplevel()

    window.title("Project Management")
    window.geometry("1150x700")
    window.configure(bg="#F5F7FA")

    # ================= HEADER =================

    header = tk.Frame(window, bg="#861F41", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="Project Management",
        bg="#861F41",
        fg="white",
        font=("Segoe UI", 20, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        header,
        text="Add, Update and Delete Projects",
        bg="#861F41",
        fg="white",
        font=("Segoe UI", 10)
    ).pack()

    # ================= MAIN CONTENT =================

    content = tk.Frame(window, bg="#F5F7FA")
    content.pack(fill="both", expand=True, padx=20, pady=20)

    # ---------- LEFT SIDE (FORM) ----------

    form = tk.LabelFrame(
        content,
        text=" Project Information ",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=15,
        bg="white"
    )

    form.pack(side="left", fill="y")

    labels = [
        "Project ID",
        "Name",
        "Description",
        "Funding Amount",
        "Status",
        "Start Date (YYYY-MM-DD)",
        "End Date (YYYY-MM-DD)",
        "Sponsor ID"
    ]

    entries = {}

    for i, label in enumerate(labels):

        tk.Label(
            form,
            text=label,
            bg="white",
            font=("Segoe UI", 10)
        ).grid(row=i, column=0, sticky="w", pady=8)

        entry = ttk.Entry(form, width=30)

        entry.grid(row=i, column=1, pady=8)

        entries[label] = entry

    # ---------- BUTTONS ----------

    button_frame = tk.Frame(form, bg="white")
    button_frame.grid(row=len(labels) + 1, column=0, columnspan=2, pady=20)

    tk.Button(
        button_frame,
        text="Add",
        bg="#2E8B57",
        fg="white",
        width=12,
        command=lambda: add_project(entries, tree)
        ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Update",
        bg="#E87722",
        fg="white",
        width=12,
        command=lambda: update_project(entries, tree)
        ).grid(row=0, column=1, padx=5)

    tk.Button(
        button_frame,
        text="Delete",
        bg="#C0392B",
        fg="white",
        width=12,
        command=lambda: delete_project(entries, tree)
        ).grid(row=0, column=2, padx=5)

    # ---------- RIGHT SIDE (TABLE) ----------

    table_frame = tk.LabelFrame(
        content,
        text=" Existing Projects ",
        font=("Segoe UI", 11, "bold"),
        padx=10,
        pady=10,
        bg="white"
    )

    table_frame.pack(side="right", fill="both", expand=True, padx=(20, 0))

    columns = (
        "ID",
        "Name",
        "Description",
        "Funding Amount",
        "Status",
        "Start Date",
        "End Date",
        "Sponsor ID"
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

    hscrollbar = ttk.Scrollbar(
        table_frame,
        orient="horizontal",
        command=tree.xview
    )

    tree.configure(yscrollcommand=scrollbar.set, xscrollcommand=hscrollbar.set)

    scrollbar.pack(side="right", fill="y")
    hscrollbar.pack(side="bottom", fill="x")
    tree.pack(fill="both", expand=True)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=110)

    load_projects(tree)

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
        "Project ID",
        "Name",
        "Description",
        "Funding Amount",
        "Status",
        "Start Date (YYYY-MM-DD)",
        "End Date (YYYY-MM-DD)",
        "Sponsor ID"
    ]

    for field, value in zip(fields, values):
        entries[field].delete(0, tk.END)
        entries[field].insert(0, value)


def clear_form(entries):
    for entry in entries.values():
        entry.delete(0, tk.END)


def add_project(entries, tree):

    try:
        conn = open_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO PROJECT
        (ProjectID, PName, PDescription, FundingAmount, Status, StartDate, EndDate, SponsorID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        project_id = entries["Project ID"].get().strip()
        name = entries["Name"].get().strip()
        description = entries["Description"].get().strip()
        funding = entries["Funding Amount"].get().strip()
        status = entries["Status"].get().strip()
        start_date = entries["Start Date (YYYY-MM-DD)"].get().strip()
        end_date = entries["End Date (YYYY-MM-DD)"].get().strip()
        sponsor_id = entries["Sponsor ID"].get().strip()

        # End Date is optional (NULL allowed), everything else is required
        required = [project_id, name, funding, status, start_date, sponsor_id]

        if any(value == "" for value in required):
            messagebox.showwarning(
                "Missing Information",
                "Please complete all required fields (End Date may be left blank)."
            )
            return

        values = (
            int(project_id),
            name,
            description if description != "" else None,
            float(funding),
            status,
            start_date,
            end_date if end_date != "" else None,
            int(sponsor_id)
        )

        cursor.execute(sql, values)

        conn.commit()
        load_projects(tree)
        clear_form(entries)

        messagebox.showinfo(
            "Success",
            "Project added successfully!"
        )

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


def update_project(entries, tree):

    try:
        project_id = entries["Project ID"].get().strip()
        name = entries["Name"].get().strip()
        description = entries["Description"].get().strip()
        funding = entries["Funding Amount"].get().strip()
        status = entries["Status"].get().strip()
        start_date = entries["Start Date (YYYY-MM-DD)"].get().strip()
        end_date = entries["End Date (YYYY-MM-DD)"].get().strip()
        sponsor_id = entries["Sponsor ID"].get().strip()

        required = [project_id, name, funding, status, start_date, sponsor_id]

        if any(value == "" for value in required):
            messagebox.showwarning(
                "Missing Information",
                "Please select a project and complete all required fields."
            )
            return

        conn = open_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE PROJECT
        SET PName = %s,
            PDescription = %s,
            FundingAmount = %s,
            Status = %s,
            StartDate = %s,
            EndDate = %s,
            SponsorID = %s
        WHERE ProjectID = %s
        """

        values = (
            name,
            description if description != "" else None,
            float(funding),
            status,
            start_date,
            end_date if end_date != "" else None,
            int(sponsor_id),
            int(project_id)
        )

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showwarning(
                "Not Found",
                f"No project found with ID {project_id}."
            )
        else:
            load_projects(tree)
            clear_form(entries)

            messagebox.showinfo(
                "Success",
                "Project updated successfully!"
            )

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


def delete_project(entries, tree):

    try:
        project_id = entries["Project ID"].get().strip()

        if project_id == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select a project to delete."
            )
            return

        conn = open_connection()
        cursor = conn.cursor()

        # Check how many dependent rows exist across DELIVERABLE and PROJECT_MEMBERSHIP
        cursor.execute(
            "SELECT COUNT(*) FROM DELIVERABLE WHERE ProjectID = %s",
            (project_id,)
        )
        deliverable_count = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM PROJECT_MEMBERSHIP WHERE ProjectID = %s",
            (project_id,)
        )
        membership_count = cursor.fetchone()[0]

        if deliverable_count > 0 or membership_count > 0:
            warning = (
                f"Project ID {project_id} has {deliverable_count} linked "
                f"deliverable(s) and {membership_count} linked researcher "
                f"membership(s).\n\n"
                f"Deleting it will also remove those records. "
                f"This cannot be undone. Continue?"
            )
        else:
            warning = f"Are you sure you want to delete project ID {project_id}?"

        confirm = messagebox.askyesno("Confirm Delete", warning)

        if not confirm:
            return

        # Remove dependent rows first, then the project itself
        cursor.execute(
            "DELETE FROM DELIVERABLE WHERE ProjectID = %s",
            (project_id,)
        )
        cursor.execute(
            "DELETE FROM PROJECT_MEMBERSHIP WHERE ProjectID = %s",
            (project_id,)
        )
        cursor.execute(
            "DELETE FROM PROJECT WHERE ProjectID = %s",
            (project_id,)
        )
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showwarning(
                "Not Found",
                f"No project found with ID {project_id}."
            )
        else:
            load_projects(tree)
            clear_form(entries)

            messagebox.showinfo(
                "Success",
                "Project deleted successfully!"
            )

    except Exception as e:
        conn.rollback()
        messagebox.showerror(
            "Database Error",
            str(e)
        )