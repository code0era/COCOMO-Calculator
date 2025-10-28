# COCOMO Calculator – Software Cost Estimation Tool

## Overview

The **COCOMO Calculator** is a Python-based GUI application designed to estimate software project costs, effort, development time, and staffing based on the **Constructive Cost Model (COCOMO)** developed by **Barry Boehm**. This tool provides a user-friendly interface for project managers, software engineers, and students to calculate **project metrics**, generate **professional reports**, and visualize results using graphs.

The project uses **Tkinter** for the GUI, **Python-docx** for report generation, and **Matplotlib** for graph plotting. It incorporates **cost driver multipliers** (EAF) for precise calculations across different project types: **Organic, Semi-Detached, and Embedded**.

---

## Features

### 1. Project Estimation

* Enter **project name**, **size (KLOC)**, and **project type**.
* Choose **cost drivers** (EAF inputs) from dropdowns.
* Automatically calculates:

  * **Effort (Person-Months)**
  * **Development Time (Months)**
  * **Average Staffing**
  * **EAF (Effort Adjustment Factor)**

### 2. Professional Report Generation

* Generates a **DOCX report** with a structured layout:

  * **Header** with project name and timestamp
  * **Project Information** including type, size, and COCOMO coefficients (A, B, C, D)
  * **Outputs** including calculated values and ceiling values
  * **Formulas** used for calculations
  * **Cost Drivers / EAF** values with serial numbers
* Saved automatically in the **current directory** or a specified folder.

### 3. Graph Visualization

* Generates **bar graphs** for all output metrics (Effort, Duration, Staff).
* Saves graph images automatically with project name.
* Can be displayed directly in the application or embedded in reports.

### 4. Knowledge Section

* Displays **all selected cost drivers and their multipliers** in a clear 3x5 grid.
* Helps users understand how each input affects the calculations.

### 5. Information Section

* Provides **full-screen information** about COCOMO and software estimation concepts.

### 6. User-Friendly GUI

* Built with **Tkinter** using a modern layout.
* Left pane: Project inputs and cost drivers.
* Right pane: Estimated values, graphs, and report generation.
* Clean fonts and colors for readability.

---

## Installation

### Requirements

* Python 3.8+
* Packages:

```bash
pip install tk
pip install python-docx
pip install matplotlib
```

### Steps

1. Clone or download the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd cocomo-calculator
```

3. Run the application:

```bash
python gui.py
```

---

## Usage

1. **Enter Project Details**:

   * Project Name
   * Size in KLOC
   * Select Project Type (Organic, Semi-Detached, Embedded)

2. **Select Cost Drivers (EAF inputs)**:

   * Choose from dropdowns for 15 cost drivers.
   * Default is “Nominal”.

3. **Calculate**:

   * Click **Calculate** to display estimated Effort, Duration, and Staffing.
   * See selected cost drivers in the “KNOW IT!” section.

4. **Generate Report**:

   * Click **Generate Report** to create a professional DOCX report.
   * Report includes all formulas, outputs, and cost driver details.

5. **Generate Graph**:

   * Click **Generate Graph** to plot Effort, Duration, and Staffing.
   * Graph saved as a PNG image for reference or embedding.

6. **View COCOMO Info**:

   * Click **Know About COCOMO** to open a full-screen explanation of COCOMO and software estimation.

---

## COCOMO Model Details

### Project Types

| Type          | Description                                    |
| ------------- | ---------------------------------------------- |
| Organic       | Small, simple projects with small teams        |
| Semi-Detached | Medium projects with mixed experience levels   |
| Embedded      | Large, complex projects with tight constraints |

### Coefficients (A, B, C, D)

* **Organic**: 2.4, 1.05, 2.5, 0.38
* **Semi-Detached**: 3.0, 1.12, 2.5, 0.35
* **Embedded**: 3.6, 1.20, 2.5, 0.32

### Formulas

* Effort (PM) = A \* (KLOC ^ B) \* EAF
* Duration (Months) = C \* (Effort ^ D)
* Staffing = Effort / Duration

---

## Project Structure

```
cocomo-calculator/
│
├─ gui.py             # Main application GUI
├─ cocomo.py          # COCOMO calculation logic
├─ data_handler.py    # Cost driver multipliers loader
├─ report.py          # DOCX report generator
├─ graph.py           # Graph plotting module
├─ info.py            # COCOMO information window
├─ README.md          # Project documentation
└─ reports/           # Folder to save reports and graphs
```

---

## Future Improvements

* Add **file export** as PDF directly from the DOCX report.
* Embed **graphs into the report automatically**.
* Add **interactive sliders** for cost drivers.
* Include **historical project data** for comparison and analysis.
* Multi-language support for international teams.

---

## Credits

* **COCOMO Model**: Barry Boehm
* **Python Libraries**: Tkinter, python-docx, Matplotlib
* Developed as a project **Product From CodeEra**.

---

## License

* MIT License (open-source) – You can freely use, modify, and distribute.
