import tkinter as tk
from tkinter import ttk, messagebox

from db_connection import open_connection

from researcher import open_researcher_window
from project import open_project_window
from publication import open_publication_window
from relationship_management import open_relationship_window
from statistics_window import open_statistics_window


def get_dashboard_stats():
    """Pull the headline counts shown across the top of the dashboard."""

    stats = {
        "researchers": 0,
        "projects": 0,
        "publications": 0,
        "sponsors": 0
    }

    try:
        conn = open_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM RESEARCHER")
        stats["researchers"] = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM PROJECT")
        stats["projects"] = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM PUBLICATION")
        stats["publications"] = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM SPONSOR")
        stats["sponsors"] = cursor.fetchone()[0]

        cursor.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

    return stats


def open_main_menu(parent):

    menu = tk.Toplevel(parent)
    menu.title("Main Dashboard")
    menu.geometry("950x760")
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
        text="Dashboard",
        bg="#861F41",
        fg="white",
        font=("Segoe UI", 11)
    ).pack()

    # ---------- Scrollable Body ----------
    # Everything below the header lives inside a canvas so the dashboard
    # scrolls instead of clipping content when the window is small or the
    # screen resolution is low.

    body_container = tk.Frame(menu, bg="#F5F7FA")
    body_container.pack(fill="both", expand=True)

    canvas = tk.Canvas(body_container, bg="#F5F7FA", highlightthickness=0)
    v_scrollbar = ttk.Scrollbar(body_container, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=v_scrollbar.set)

    v_scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    body = tk.Frame(canvas, bg="#F5F7FA")
    body_window = canvas.create_window((0, 0), window=body, anchor="nw")

    def on_body_configure(event):
        # Update the scrollable region whenever the body's content changes size
        canvas.configure(scrollregion=canvas.bbox("all"))

    body.bind("<Configure>", on_body_configure)

    def on_canvas_configure(event):
        # Keep the inner frame the same width as the visible canvas
        canvas.itemconfig(body_window, width=event.width)

    canvas.bind("<Configure>", on_canvas_configure)

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_mousewheel_linux(event):
        canvas.yview_scroll(-1 if event.num == 4 else 1, "units")

    # Windows / macOS
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    # Linux
    canvas.bind_all("<Button-4>", on_mousewheel_linux)
    canvas.bind_all("<Button-5>", on_mousewheel_linux)

    def on_menu_close():
        # bind_all is global, so release it before the window disappears —
        # otherwise scrolling in other windows would silently break.
        canvas.unbind_all("<MouseWheel>")
        canvas.unbind_all("<Button-4>")
        canvas.unbind_all("<Button-5>")
        menu.destroy()

    menu.protocol("WM_DELETE_WINDOW", on_menu_close)

    # ---------- Stat Cards ----------

    stats = get_dashboard_stats()

    stats_frame = tk.Frame(body, bg="#F5F7FA")
    stats_frame.pack(fill="x", padx=30, pady=(25, 10))

    card_specs = [
        ("Researchers", stats["researchers"], "#861F41"),
        ("Projects", stats["projects"], "#2C7BE5"),
        ("Publications", stats["publications"], "#2E8B57"),
        ("Sponsors", stats["sponsors"], "#E87722"),
    ]

    for col, (label, value, color) in enumerate(card_specs):

        stats_frame.grid_columnconfigure(col, weight=1)

        card = tk.Frame(
            stats_frame,
            bg="white",
            width=170,
            height=100,
            relief="solid",
            bd=1
        )
        card.grid(row=0, column=col, padx=10, sticky="ew")
        card.grid_propagate(False)

        tk.Label(
            card,
            text=label,
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg="#333333"
        ).pack(pady=(15, 5))

        tk.Label(
            card,
            text=str(value),
            font=("Segoe UI", 28, "bold"),
            fg=color,
            bg="white"
        ).pack()

    # ---------- Divider ----------

    divider = tk.Frame(body, bg="#D9DEE4", height=2)
    divider.pack(fill="x", padx=30, pady=20)

    tk.Label(
        body,
        text="Navigation",
        bg="#F5F7FA",
        fg="#555555",
        font=("Segoe UI", 11, "bold")
    ).pack(anchor="w", padx=35)

    # ---------- Content (Navigation Grid) ----------

    content = tk.Frame(body, bg="#F5F7FA")
    content.pack(expand=True, pady=(10, 30))

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
        text="📚\n\nPublications\n\nManage Publications",
        width=22,
        height=8,
        bg="white",
        font=("Segoe UI", 11, "bold"),
        command=open_publication_window,
        cursor="hand2"
    )

    relationship_btn = tk.Button(
        content,
        text="🔗\n\nRelationships\n\nManage Assignments",
        width=22,
        height=8,
        bg="white",
        font=("Segoe UI", 11, "bold"),
        command=open_relationship_window,
        cursor="hand2"
    )

    reports_btn = tk.Button(
        content,
        text="📈\n\nReports\n\nView Statistics",
        width=22,
        height=8,
        bg="white",
        font=("Segoe UI", 11, "bold"),
        command=open_statistics_window,
        cursor="hand2"
    )

    exit_btn = tk.Button(
        content,
        text="🚪\n\nExit\n\nClose Application",
        width=22,
        height=8,
        bg="white",
        font=("Segoe UI", 11, "bold"),
        command=parent.destroy,
        cursor="hand2"
    )

    researcher_btn.grid(row=0, column=0, padx=25, pady=15)
    project_btn.grid(row=0, column=1, padx=25, pady=15)
    publication_btn.grid(row=1, column=0, padx=25, pady=15)
    relationship_btn.grid(row=1, column=1, padx=25, pady=15)
    reports_btn.grid(row=2, column=0, padx=25, pady=15)
    exit_btn.grid(row=2, column=1, padx=25, pady=15)