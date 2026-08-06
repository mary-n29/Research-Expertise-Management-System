def load_researchers(tree):
    from db_connection import open_connection
    import tkinter as tk
    conn = open_connection()
    cursor = conn.cursor()

    # Clear existing rows
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("""
        SELECT ResearcherID,
               FName,
               LName,
               Department,
               Position
        FROM RESEARCHER
        ORDER BY ResearcherID
    """)

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)