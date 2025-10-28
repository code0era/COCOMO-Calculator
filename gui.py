# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from cocomo import COCOMO
from data_handler import load_multipliers
from docx import Document
from graph import plot_results
import math
from info import show_cocomo_info 
from report import generate_report

class COCOMOApp:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.state("zoomed")  # Fullscreen

        self.multipliers = load_multipliers()
        self.cocomo = COCOMO()
        self.inputs = {}

        self.create_main_window()

    def create_main_window(self):
        # --- Main Header ---
        header_frame = tk.Frame(self.root, bg="#ffffff")  # deep blue background
        header_frame.pack(fill="x")

        header_label = tk.Label(
            header_frame,
            text="COCOMO CALCULATOR",
            font=("Roboto", 24, "bold"),
            bg="#003366",  # same as frame
            fg="#ffffff",    # white text
            pady=15
            )
        
        header_label.pack(fill="x")
        main_frame = tk.Frame(self.root, bg="#f4f6f8")
        main_frame.pack(fill="both", expand=True)
        


                # --- Left Frame ---
        left_frame = tk.Frame(main_frame, width=850, bg="#ffffff")
        left_frame.pack(side="left", fill="y")       # only fill vertically
        left_frame.pack_propagate(False)             # keep width fixed at 300

        # Left Heading
        left_heading = tk.Label(
            left_frame, text="ESTIMATE YOUR PROJECT",
            font=("Roboto", 16, "bold"),
            bg="#0073e6", fg="white", pady=10
        )
        left_heading.pack(fill="x")

        # Scrollable Inputs
        canvas = tk.Canvas(left_frame, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- Project Name Section ---
        project_frame = tk.LabelFrame(
            scrollable_frame,
            text="PROJECT NAME",
            font=("Roboto", 12, "bold"),
            bg="#75bef3",
            fg="#220280",
            bd=2, relief="ridge", padx=10, pady=10
        )
        project_frame.pack(pady=10, fill="x")

        tk.Label(project_frame, text="Enter Project Name:",
                font=("Roboto", 12, "bold"),width=60, bg="#75bef3", fg="#220280").pack(pady=5, fill="x")
        self.project_name_entry = tk.Entry(project_frame, font=("Roboto", 12))
        self.project_name_entry.pack(pady=5, fill="x")

        # --- Project Size & Type ---
        tk.Label(scrollable_frame, text="Enter Project Size (KLOC):",
                font=("Roboto", 12, "bold"), width=40,bg="white").pack(pady=5, fill="x")
        self.kloc_entry = tk.Entry(scrollable_frame, width=40,font=("Roboto", 12))
        self.kloc_entry.pack(pady=15)

        tk.Label(scrollable_frame, text="Select Project Type:",
                font=("Roboto", 12, "bold"),width=40, bg="white").pack(pady=5, fill="x")
        self.project_type = ttk.Combobox(scrollable_frame,width=40, values=["organic", "semi-detached", "embedded"])
        self.project_type.pack(pady=15)
        self.project_type.set("organic")  # default selection

        # --- Cost Drivers ---
        drivers_frame = tk.LabelFrame(
            scrollable_frame, text="Cost Drivers (EAF Inputs)",
            font=("Roboto", 14, "bold"),
            bg="white", fg="#003366", bd=3, relief="groove", padx=10, pady=10
        )
        drivers_frame.pack(pady=10, fill="x")

        row, col = 0, 0
        for i, (driver, ratings) in enumerate(self.multipliers.items()):
            tk.Label(drivers_frame, text=driver, anchor="w", bg="white", fg="black",
                    font=("Roboto", 12)).grid(row=row, column=col*2, padx=5, pady=5, sticky="ew")
            cb = ttk.Combobox(drivers_frame, values=list(ratings.keys()))
            cb.set("Nominal")
            cb.grid(row=row, column=col*2 + 1, padx=5, pady=5, sticky="ew")
            self.inputs[driver] = cb

            # make columns expand evenly
            drivers_frame.grid_columnconfigure(col*2, weight=1)
            drivers_frame.grid_columnconfigure(col*2 + 1, weight=1)

            row += 1
            if row == 5:
                row = 0
                col += 1

        # --- Calculate Button ---

        tk.Button(scrollable_frame, text="Calculate",
                command=self.show_results,
                bg="#003366", fg="white",
                font=("Roboto", 12, "bold"),
                activebackground="#003d99").pack(fill="both")


        # --- Know About COCOMO Button ---
        tk.Button(scrollable_frame, text="Know About COCOMO",
                  command=show_cocomo_info,
                  bg="#003366", fg="white",
                  font=("Roboto", 12, "bold"), activebackground="#0052a6").pack(pady=10)





        # --- Description Section ---
        desc_label = tk.Label(
            self.root,
            text="COCOMO (Constructive Cost Model) is a software cost estimation model developed by Barry Boehm.\n"
                 "It helps predict effort, development time, and cost based on project size and complexity.\n"
                 "Product From CodeEra!\n"
                 "All rights are reserved!",

            font=("Open Sans", 8),
            bg="#cce6ff",
            fg="black",
            wraplength=1500,
            justify="center",
            padx=10,
            pady=10
        )
        desc_label.pack(fill="x")






        # --- Right Frame ---
        right_frame = tk.Frame(main_frame, bg="#ffffff")
        right_frame.pack(side="right", fill="both", expand=True)

        right_heading = tk.Label(
            right_frame, text="ESTIMATED VALUES",
            font=("Roboto", 16, "bold"),
            bg="#28a745", fg="white", pady=10
        )
        right_heading.pack(fill="x")
        self.output_frame = right_frame


             # Report Button Function
    def report_button_click(self):
        try:
            project_name = self.project_name_entry.get().strip() or "Unnamed Project"
            kloc_val = float(self.kloc_entry.get())
            project_type = self.project_type.get()

            # Prepare cost drivers
            cost_drivers = {}
            for drv, cb in self.inputs.items():
                selected = cb.get()
                multiplier = self.multipliers[drv].get(selected, 1.0)
                cost_drivers[drv] = multiplier

            # Calculate results
            results = self.cocomo.calculate_effort(kloc_val, project_type, cost_drivers)

            # Optional: generate graph before report
            graph_path = f"{project_name.replace(' ', '_')}_graph.png"
            plot_results(results, project_name, save_path=graph_path)  # modify plot_results to save

            # Generate report
            filename = generate_report(
                project_name=project_name,
                project_type=project_type,
                kloc=kloc_val,
                results=results,
                cost_drivers=cost_drivers,
                cocomo=self.cocomo,
                graph_path=graph_path
            )

            messagebox.showinfo("Report Generated", f"Report successfully saved as:\n{filename}")

        except Exception as e:
            messagebox.showerror("Error", str(e))



    def show_results(self):
        try:
            kloc = float(self.kloc_entry.get())
            ptype = self.project_type.get()

            cost_drivers = {}
            for drv, cb in self.inputs.items():
                selected = cb.get()
                multiplier = self.multipliers[drv].get(selected, 1.0)
                cost_drivers[drv] = multiplier

            results = self.cocomo.calculate_effort(kloc, ptype, cost_drivers)

            # Clear previous results
            for widget in self.output_frame.winfo_children():
                if widget != self.output_frame.pack_slaves()[0]:
                    widget.destroy()

            # --- RESULTS Table ---
            project_name = self.project_name_entry.get().strip() or "Unnamed Project"

            results_frame = tk.LabelFrame(
                self.output_frame,
                text=f"RESULTS - {project_name}",
                font=("Roboto", 26, "bold"),
                bg="#e8f5e9",
                fg="#333333",
                bd=3,
                relief="ridge",
                padx=15,
                pady=15
            )
            results_frame.pack(fill="x", pady=10)

            # --- Header Row ---
            tk.Label(results_frame, text="Metric", font=("Roboto", 14, "bold"),
                     bg="#a5d6a7", fg="#333333").grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
            tk.Label(results_frame, text="Value", font=("Roboto", 14, "bold"),
                     bg="#a5d6a7", fg="#333333").grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
            tk.Label(results_frame, text="Ceiling Value", font=("Roboto", 14, "bold"),
                     bg="#a5d6a7", fg="#333333").grid(row=0, column=2, padx=10, pady=5, sticky="nsew")

            # --- Grid Rows for Results ---
            for i, (key, val) in enumerate(results.items(), start=1):
                bg_color = "#ffffff" if i % 2 == 1 else "#f1f8e9"
                tk.Label(results_frame, text=key, font=("Roboto", 12), bg=bg_color, anchor="w").grid(row=i, column=0, sticky="nsew", padx=10, pady=3)
                tk.Label(results_frame, text=val, font=("Roboto", 12), bg=bg_color, anchor="w").grid(row=i, column=1, sticky="nsew", padx=10, pady=3)
                tk.Label(results_frame, text=math.ceil(val), font=("Roboto", 12), bg=bg_color, anchor="w").grid(row=i, column=2, sticky="nsew", padx=10, pady=3)

            # --- Make columns expand evenly ---
            results_frame.grid_columnconfigure(0, weight=1)
            results_frame.grid_columnconfigure(1, weight=1)
            results_frame.grid_columnconfigure(2, weight=1)

            # --- KNOW IT! Section (3x5 grid) ---
            know_frame = tk.LabelFrame(
                self.output_frame, text="KNOW IT!",
                font=("Roboto", 14, "bold"),
                bg="#e6f2ff", fg="#003366", bd=2, relief="groove", padx=10, pady=10
            )
            know_frame.pack(fill="both", pady=15, anchor="w")

            row, col = 0, 0
            for i, (drv, val) in enumerate(cost_drivers.items()):
                rating_selected = self.inputs[drv].get()
                multiplier_val = self.multipliers[drv][rating_selected]
                lbl_text = f"{drv}: {rating_selected} → {multiplier_val}"
                tk.Label(
                    know_frame, text=lbl_text,
                    font=("Roboto", 9),
                    bg="#e6f2ff", anchor="w"
                ).grid(row=row, column=col, sticky="w", padx=5, pady=2)

                row += 1
                if row == 5:
                    row = 0
                    col += 1


            # --- Action Buttons ---
            btn_frame = tk.Frame(self.output_frame, bg="#e6f2ff")
            btn_frame.pack(pady=10)
            tk.Button(btn_frame, text="Generate Report",
                command=self.report_button_click,
                bg="#003366", fg="white", font=("Roboto", 11, "bold")).pack(side="left", padx=5)
            
            tk.Button(btn_frame, text="Generate Graph",
                      command=lambda: plot_results(results, self.project_name_entry.get()),
                      bg="#003366", fg="white", font=("Roboto", 11, "bold")).pack(side="left", padx=5)


        except Exception as e:
            messagebox.showerror("Error", str(e))

      