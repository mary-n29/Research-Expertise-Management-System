def load_projects(tree):
    from db_connection import open_connection
    import tkinter as tk
    conn = open_connection()
    cursor = conn.cursor()

    # Clear existing rows
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("""
        SELECT ProjectID,
               PName,
               PDescription,
               FundingAmount,
               Status,
               StartDate,
               EndDate,
               SponsorID
        FROM PROJECT
        ORDER BY ProjectID
    """)

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)