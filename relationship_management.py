import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from db_connection import open_connection


def open_relationship_window():

    conn = open_connection()
    cursor = conn.cursor()

    window = tk.Toplevel()
    window.title("Relationship Management")
    window.geometry("950x650")
    window.configure(bg="#F5F7FA")

    # ================= Header ==================

    header = tk.Frame(window, bg="#861F41", height=80)
    header.pack(fill="x")

    tk.Label(
        header,
        text="Relationship Management",
        bg="#861F41",
        fg="white",
        font=("Segoe UI",20,"bold")
    ).pack(pady=20)

    notebook = ttk.Notebook(window)
    notebook.pack(fill="both", expand=True, padx=15, pady=15)

    ####################################################
    # TAB 1
    ####################################################

    project_tab = ttk.Frame(notebook)
    notebook.add(project_tab, text="Project Membership")

    ####################################################
    # TAB 2
    ####################################################

    publication_tab = ttk.Frame(notebook)
    notebook.add(publication_tab, text="Publication Authors")

    ####################################################
    # -------- PROJECT MEMBERSHIP TAB ----------
    ####################################################

    ttk.Label(project_tab,text="Researcher").grid(row=0,column=0,padx=10,pady=10)

    researcher_combo = ttk.Combobox(project_tab,width=35)
    researcher_combo.grid(row=0,column=1)

    ttk.Label(project_tab,text="Project").grid(row=1,column=0,padx=10,pady=10)

    project_combo = ttk.Combobox(project_tab,width=35)
    project_combo.grid(row=1,column=1)

    ttk.Label(project_tab,text="Join Date (YYYY-MM-DD)").grid(row=2,column=0,padx=10,pady=10)

    join_entry = ttk.Entry(project_tab,width=38)
    join_entry.grid(row=2,column=1)

    # Auto-fill today's date so the user doesn't have to type it every time
    join_entry.insert(0, date.today().strftime("%Y-%m-%d"))

    ####################################################
    # Load researchers
    ####################################################

    cursor.execute("""
        SELECT ResearcherID,
               CONCAT(FName,' ',LName)
        FROM RESEARCHER
    """)

    researchers = cursor.fetchall()

    researcher_combo["values"] = [
        f"{r[0]} - {r[1]}"
        for r in researchers
    ]

    ####################################################
    # Load projects
    ####################################################

    cursor.execute("""
        SELECT ProjectID,PName
        FROM PROJECT
    """)

    projects = cursor.fetchall()

    project_combo["values"] = [
        f"{p[0]} - {p[1]}"
        for p in projects
    ]

    ####################################################
    # Treeview
    ####################################################

    tree1 = ttk.Treeview(
        project_tab,
        columns=("Project","Researcher","JoinDate"),
        show="headings",
        height=10
    )

    tree1.heading("Project",text="Project")
    tree1.heading("Researcher",text="Researcher")
    tree1.heading("JoinDate",text="Join Date")

    tree1.column("Project", width=280)
    tree1.column("Researcher", width=250)
    tree1.column("JoinDate", width=120, anchor="center")

    tree1.grid(row=4,column=0,columnspan=3,padx=10,pady=20)

    ####################################################
    # Load memberships
    ####################################################

    # Keep the underlying ProjectID/ResearcherID for each row so Remove
    # doesn't have to re-parse names back into IDs.
    def load_members():

        for row in tree1.get_children():
            tree1.delete(row)

        cursor.execute("""

        SELECT
        P.ProjectID,
        R.ResearcherID,
        P.PName,
        CONCAT(R.FName,' ',R.LName),
        PM.JoinDate

        FROM PROJECT_MEMBERSHIP PM

        JOIN PROJECT P

        ON PM.ProjectID=P.ProjectID

        JOIN RESEARCHER R

        ON PM.ResearcherID=R.ResearcherID

        """)

        for row in cursor.fetchall():

            project_id, researcher_id, pname, rname, join_date = row

            tree1.insert(
                "",
                tk.END,
                values=(pname, rname, join_date),
                tags=(f"{project_id}|{researcher_id}",)
            )

    ####################################################
    # Assign researcher
    ####################################################

    def assign_member():

        try:

            researcher = int(
                researcher_combo.get().split("-")[0].strip()
            )

            project = int(
                project_combo.get().split("-")[0].strip()
            )

            date_val = join_entry.get()

            # Prevent duplicate assignments before inserting
            cursor.execute("""

            SELECT *
            FROM PROJECT_MEMBERSHIP
            WHERE ProjectID=%s
            AND ResearcherID=%s

            """, (project, researcher))

            if cursor.fetchone():
                messagebox.showwarning(
                    "Duplicate Assignment",
                    "This researcher is already assigned to this project."
                )
                return

            cursor.execute("""

            INSERT INTO PROJECT_MEMBERSHIP

            VALUES(%s,%s,%s)

            """,(project,researcher,date_val))

            conn.commit()

            load_members()

            messagebox.showinfo(
                "Success",
                "Researcher successfully assigned to project."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    ####################################################
    # Remove membership
    ####################################################

    def remove_member():

        selected = tree1.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select a membership to remove."
            )
            return

        try:
            item = selected[0]
            project_id, researcher_id = tree1.item(item, "tags")[0].split("|")

            confirm = messagebox.askyesno(
                "Confirm Removal",
                "Remove this researcher from the project?"
            )

            if not confirm:
                return

            cursor.execute("""

            DELETE
            FROM PROJECT_MEMBERSHIP
            WHERE ProjectID=%s
            AND ResearcherID=%s

            """, (project_id, researcher_id))

            conn.commit()

            load_members()

            messagebox.showinfo(
                "Removed",
                "Researcher removed from project."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    ttk.Button(
        project_tab,
        text="Assign Researcher",
        command=assign_member
    ).grid(row=3,column=1,pady=10)

    ttk.Button(
        project_tab,
        text="Remove Selected",
        command=remove_member
    ).grid(row=3,column=2,pady=10)

    load_members()

    ####################################################
    # -------- PUBLICATION AUTHORS ----------
    ####################################################

    ttk.Label(publication_tab,text="Researcher").grid(row=0,column=0,padx=10,pady=10)

    researcher2 = ttk.Combobox(publication_tab,width=35)

    researcher2.grid(row=0,column=1)

    researcher2["values"]=researcher_combo["values"]

    ttk.Label(publication_tab,text="Publication").grid(row=1,column=0,padx=10,pady=10)

    publication_combo=ttk.Combobox(publication_tab,width=35)

    publication_combo.grid(row=1,column=1)

    cursor.execute("""

    SELECT PublicationID,
           PubTitle

    FROM PUBLICATION

    """)

    pubs=cursor.fetchall()

    publication_combo["values"]=[
        f"{p[0]} - {p[1]}"
        for p in pubs
    ]

    tree2=ttk.Treeview(
        publication_tab,
        columns=("Publication","Author"),
        show="headings",
        height=10
    )

    tree2.heading("Publication",text="Publication")
    tree2.heading("Author",text="Author")

    tree2.column("Publication", width=350)
    tree2.column("Author", width=250)

    tree2.grid(row=3,column=0,columnspan=3,padx=10,pady=20)

    def load_authors():

        for row in tree2.get_children():

            tree2.delete(row)

        cursor.execute("""

        SELECT
        P.PublicationID,
        R.ResearcherID,
        PubTitle,
        CONCAT(FName,' ',LName)

        FROM PUBLICATION_AUTHOR PA

        JOIN PUBLICATION P

        ON PA.PublicationID=P.PublicationID

        JOIN RESEARCHER R

        ON PA.ResearcherID=R.ResearcherID

        """)

        for row in cursor.fetchall():

            pub_id, researcher_id, pub_title, rname = row

            tree2.insert(
                "",
                tk.END,
                values=(pub_title, rname),
                tags=(f"{pub_id}|{researcher_id}",)
            )

    def assign_author():

        try:

            researcher=int(
                researcher2.get().split("-")[0].strip()
            )

            publication=int(
                publication_combo.get().split("-")[0].strip()
            )

            # Prevent duplicate authorship before inserting
            cursor.execute("""

            SELECT *
            FROM PUBLICATION_AUTHOR
            WHERE PublicationID=%s
            AND ResearcherID=%s

            """, (publication, researcher))

            if cursor.fetchone():
                messagebox.showwarning(
                    "Duplicate Author",
                    "This author is already assigned to this publication."
                )
                return

            cursor.execute("""

            INSERT INTO PUBLICATION_AUTHOR

            VALUES(%s,%s)

            """,(publication,researcher))

            conn.commit()

            load_authors()

            messagebox.showinfo(
                "Success",
                "Author successfully assigned to publication."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def remove_author():

        selected = tree2.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select an author to remove."
            )
            return

        try:
            item = selected[0]
            pub_id, researcher_id = tree2.item(item, "tags")[0].split("|")

            confirm = messagebox.askyesno(
                "Confirm Removal",
                "Remove this author from the publication?"
            )

            if not confirm:
                return

            cursor.execute("""

            DELETE
            FROM PUBLICATION_AUTHOR
            WHERE PublicationID=%s
            AND ResearcherID=%s

            """, (pub_id, researcher_id))

            conn.commit()

            load_authors()

            messagebox.showinfo(
                "Removed",
                "Author removed from publication."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    ttk.Button(
        publication_tab,
        text="Assign Author",
        command=assign_author
    ).grid(row=2,column=1,pady=10)

    ttk.Button(
        publication_tab,
        text="Remove Selected",
        command=remove_author
    ).grid(row=2,column=2,pady=10)

    load_authors()