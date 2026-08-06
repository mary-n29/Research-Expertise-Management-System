import tkinter as tk
from tkinter import ttk

from tkinter import messagebox

from db_connection import open_connection
from load_publication import load_publications


def open_publication_window():

    window = tk.Toplevel()

    window.title("Publication Management")
    window.geometry("1000x700")
    window.configure(bg="#F5F7FA")

    # ================= HEADER =================

    header = tk.Frame(window, bg="#861F41", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="Publication Management",
        bg="#861F41",
        fg="white",
        font=("Segoe UI", 20, "bold")
    ).pack(pady=(20, 5))

    tk.Label(
        header,
        text="Add, Update and Delete Publications",
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
        text=" Publication Information ",
        font=("Segoe UI", 11, "bold"),
        padx=15,
        pady=15,
        bg="white"
    )

    form.pack(side="left", fill="y")

    labels = [
        "Publication ID",
        "Title",
        "Publication Date (YYYY-MM-DD)",
        "DOI"
    ]

    entries = {}

    for i, label in enumerate(labels):

        tk.Label(
            form,
            text=label,
            bg="white",
            font=("Segoe UI", 10)
        ).grid(row=i, column=0, sticky="w", pady=8)

        entry = ttk.Entry(form, width=32)

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
        command=lambda: add_publication(entries, tree)
        ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Update",
        bg="#E87722",
        fg="white",
        width=12,
        command=lambda: update_publication(entries, tree)
        ).grid(row=0, column=1, padx=5)

    tk.Button(
        button_frame,
        text="Delete",
        bg="#C0392B",
        fg="white",
        width=12,
        command=lambda: delete_publication(entries, tree)
        ).grid(row=0, column=2, padx=5)

    # ---------- RIGHT SIDE (TABLE) ----------

    table_frame = tk.LabelFrame(
        content,
        text=" Existing Publications ",
        font=("Segoe UI", 11, "bold"),
        padx=10,
        pady=10,
        bg="white"
    )

    table_frame.pack(side="right", fill="both", expand=True, padx=(20, 0))

    columns = (
        "ID",
        "Title",
        "Publication Date",
        "DOI"
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

    load_publications(tree)

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
        "Publication ID",
        "Title",
        "Publication Date (YYYY-MM-DD)",
        "DOI"
    ]

    for field, value in zip(fields, values):
        entries[field].delete(0, tk.END)
        entries[field].insert(0, value)


def clear_form(entries):
    for entry in entries.values():
        entry.delete(0, tk.END)


def add_publication(entries, tree):

    try:
        conn = open_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO PUBLICATION
        (PublicationID, PubTitle, PubDate, DOI)
        VALUES (%s, %s, %s, %s)
        """

        pub_id = entries["Publication ID"].get().strip()
        title = entries["Title"].get().strip()
        pub_date = entries["Publication Date (YYYY-MM-DD)"].get().strip()
        doi = entries["DOI"].get().strip()

        # PubDate and DOI are optional (nullable) in the schema
        if pub_id == "" or title == "":
            messagebox.showwarning(
                "Missing Information",
                "Please complete at least Publication ID and Title."
            )
            return

        values = (
            int(pub_id),
            title,
            pub_date if pub_date != "" else None,
            doi if doi != "" else None
        )

        cursor.execute(sql, values)

        conn.commit()
        load_publications(tree)
        clear_form(entries)

        messagebox.showinfo(
            "Success",
            "Publication added successfully!"
        )

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


def update_publication(entries, tree):

    try:
        pub_id = entries["Publication ID"].get().strip()
        title = entries["Title"].get().strip()
        pub_date = entries["Publication Date (YYYY-MM-DD)"].get().strip()
        doi = entries["DOI"].get().strip()

        if pub_id == "" or title == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select a publication and complete at least Title."
            )
            return

        conn = open_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE PUBLICATION
        SET PubTitle = %s,
            PubDate = %s,
            DOI = %s
        WHERE PublicationID = %s
        """

        values = (
            title,
            pub_date if pub_date != "" else None,
            doi if doi != "" else None,
            int(pub_id)
        )

        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showwarning(
                "Not Found",
                f"No publication found with ID {pub_id}."
            )
        else:
            load_publications(tree)
            clear_form(entries)

            messagebox.showinfo(
                "Success",
                "Publication updated successfully!"
            )

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


def delete_publication(entries, tree):

    try:
        pub_id = entries["Publication ID"].get().strip()

        if pub_id == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select a publication to delete."
            )
            return

        conn = open_connection()
        cursor = conn.cursor()

        # Check how many PUBLICATION_AUTHOR rows link to this publication
        cursor.execute(
            "SELECT COUNT(*) FROM PUBLICATION_AUTHOR WHERE PublicationID = %s",
            (pub_id,)
        )
        author_link_count = cursor.fetchone()[0]

        if author_link_count > 0:
            warning = (
                f"Publication ID {pub_id} has {author_link_count} linked "
                f"author record(s) in PUBLICATION_AUTHOR.\n\n"
                f"Deleting it will also remove those {author_link_count} link(s). "
                f"This cannot be undone. Continue?"
            )
        else:
            warning = f"Are you sure you want to delete publication ID {pub_id}?"

        confirm = messagebox.askyesno("Confirm Delete", warning)

        if not confirm:
            return

        # Remove dependent rows first, then the publication itself
        cursor.execute(
            "DELETE FROM PUBLICATION_AUTHOR WHERE PublicationID = %s",
            (pub_id,)
        )
        cursor.execute(
            "DELETE FROM PUBLICATION WHERE PublicationID = %s",
            (pub_id,)
        )
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showwarning(
                "Not Found",
                f"No publication found with ID {pub_id}."
            )
        else:
            load_publications(tree)
            clear_form(entries)

            messagebox.showinfo(
                "Success",
                "Publication deleted successfully!"
            )

    except Exception as e:
        conn.rollback()
        messagebox.showerror(
            "Database Error",
            str(e)
        )