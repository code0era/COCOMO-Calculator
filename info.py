# info.py
import tkinter as tk
from tkinter import ttk

def show_cocomo_info():
    info_window = tk.Toplevel()
    info_window.title("COCOMO Information")
    info_window.geometry("1400x800")
    info_window.configure(bg="white")
    info_window.state("zoomed")  # Fullscreen


    # --- Header ---
    tk.Label(info_window, text="COCOMO CALCULATOR INFO",
             font=("Roboto", 18, "bold"),
             bg="#0073e6", fg="white", pady=10).pack(fill="x")

    # --- Scrollable Frame ---
    canvas = tk.Canvas(info_window, bg="white", highlightthickness=0)
    scrollbar = ttk.Scrollbar(info_window, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="white")

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # --- COCOMO Overview ---
    overview_text = """
COCOMO (Constructive Cost Model) is a procedural software cost estimation model developed by Barry Boehm.
It estimates effort, development time, and team size based on project size and cost drivers.

There are three main types of projects:

1. Organic:
   - Small teams, familiar environments
   - Simple software with low complexity

2. Semi-Detached:
   - Medium teams, mixed experience
   - Medium complexity software

3. Embedded:
   - Large teams, tight constraints
   - Complex software with strict requirements

COCOMO Formulas:
1. Effort = a * (KLOC^b) * EAF
2. Time = c * (Effort^d)
3. Staff = Effort / Time

Without EAF:
Effort = a * (KLOC^b)
Time = c * (Effort^d)
"""

    tk.Label(scroll_frame, text=overview_text,
             font=("Roboto", 11), bg="white", justify="left", wraplength=750).pack(padx=10, pady=10)

    # --- ABCD Table ---
    tk.Label(scroll_frame, text="COCOMO ABCD Values for Project Types",
             font=("Roboto", 14, "bold"), bg="#0073e6", fg="white", pady=5).pack(fill="x", pady=5)

    table_frame = tk.Frame(scroll_frame, bg="white")
    table_frame.pack(padx=10, pady=5, fill="x")

    headers = ["Project Type", "a", "b", "c", "d"]
    for col, head in enumerate(headers):
        tk.Label(table_frame, text=head, font=("Roboto", 12, "bold"), bg="#a5d6a7", width=15, relief="ridge").grid(row=0, column=col)

    abc_values = {
        "Organic": [2.4, 1.05, 2.5, 0.38],
        "Semi-Detached": [3.0, 1.12, 2.5, 0.35],
        "Embedded": [3.6, 1.20, 2.5, 0.32]
    }

    for i, (ptype, vals) in enumerate(abc_values.items(), start=1):
        for j, val in enumerate([ptype] + vals):
            bg = "#e8f5e9" if i % 2 == 1 else "#ffffff"
            tk.Label(table_frame, text=str(val), font=("Roboto", 11), bg=bg, width=15, relief="ridge").grid(row=i, column=j)

    # --- Cost Drivers Table ---
    tk.Label(scroll_frame, text="Cost Drivers and Multipliers",
             font=("Roboto", 14, "bold"), bg="#0073e6", fg="white", pady=5).pack(fill="x", pady=5)

    drivers_frame = tk.Frame(scroll_frame, bg="white")
    drivers_frame.pack(padx=10, pady=5, fill="x")

    # Example multipliers; you can expand all
    drivers = {
    "RELY (Required Software Reliability)": [
        "Very Low: 0.75",
        "Low: 0.88",
        "Nominal: 1.0",
        "High: 1.15",
        "Very High: 1.40"
    ],
    "DATA (Database Size)": [
        "Low: 0.94",
        "Nominal: 1.0",
        "High: 1.08",
        "Very High: 1.16"
    ],
    "CPLX (Product Complexity)": [
        "Very Low: 0.70",
        "Low: 0.85",
        "Nominal: 1.0",
        "High: 1.15",
        "Very High: 1.30",
        "Extra High: 1.65"
    ],
    "TIME (Execution Time Constraint)": [
        "Nominal: 1.0",
        "High: 1.11",
        "Very High: 1.30",
        "Extra High: 1.66"
    ],
    "STOR (Main Storage Constraint)": [
        "Nominal: 1.0",
        "High: 1.06",
        "Very High: 1.21",
        "Extra High: 1.56"
    ],
    "VIRT (Virtual Machine Volatility)": [
        "Low: 0.87",
        "Nominal: 1.0",
        "High: 1.15",
        "Very High: 1.30"
    ],
    "TURN (Computer Turnaround Time)": [
        "Low: 0.87",
        "Nominal: 1.0",
        "High: 1.07",
        "Very High: 1.15"
    ],
    "ACAP (Analyst Capability)": [
        "Very Low: 1.46",
        "Low: 1.19",
        "Nominal: 1.0",
        "High: 0.86",
        "Very High: 0.71"
    ],
    "AEXP (Applications Experience)": [
        "Very Low: 1.29",
        "Low: 1.13",
        "Nominal: 1.0",
        "High: 0.91",
        "Very High: 0.82"
    ],
    "PCAP (Programmer Capability)": [
        "Very Low: 1.42",
        "Low: 1.17",
        "Nominal: 1.0",
        "High: 0.86",
        "Very High: 0.70"
    ],
    "VEXP (Virtual Machine Experience)": [
        "Very Low: 1.21",
        "Low: 1.10",
        "Nominal: 1.0",
        "High: 0.90"
    ],
    "LEXP (Language Experience)": [
        "Very Low: 1.14",
        "Low: 1.07",
        "Nominal: 1.0",
        "High: 0.95"
    ],
    "MODP (Modern Programming Practices)": [
        "Very Low: 1.24",
        "Low: 1.10",
        "Nominal: 1.0",
        "High: 0.91",
        "Very High: 0.82"
    ],
    "TOOL (Use of Software Tools)": [
        "Very Low: 1.24",
        "Low: 1.10",
        "Nominal: 1.0",
        "High: 0.91",
        "Very High: 0.83"
    ],
    "SCED (Required Development Schedule)": [
        "Very Low: 1.23",
        "Low: 1.08",
        "Nominal: 1.0",
        "High: 1.04",
        "Very High: 1.10"
    ]
}


    row = 0
    for drv, vals in drivers.items():
        tk.Label(drivers_frame, text=drv, font=("Roboto", 12, "bold"), bg="#e3f2fd", width=40, anchor="w", relief="groove").grid(row=row, column=0, sticky="w")
        row += 1
        for v in vals:
            tk.Label(drivers_frame, text=v, font=("Roboto", 10), bg="#f0f4f8", anchor="w", width=40, relief="ridge").grid(row=row, column=0, sticky="w")
            row += 1

    # --- Footer ---
    tk.Label(scroll_frame, text="All values are best true as per officail values now. Refer to official COCOMO documentation for precise multipliers.",
             font=("Roboto", 10, "italic"), bg="white", fg="#555555").pack(pady=10)
