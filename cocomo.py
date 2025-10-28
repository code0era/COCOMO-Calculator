
# Real Calculations: 

        # effort = a * (kloc ** b) * eaf
        # time = c * (effort ** d)
        # staff = effort / time

class COCOMO:
    def __init__(self):
        self.coefficients = {
            "organic": (2.4, 1.05, 2.5, 0.38),
            "semi-detached": (3.0, 1.12, 2.5, 0.35),
            "embedded": (3.6, 1.20, 2.5, 0.32)
        }

    def calculate_effort(self, kloc, project_type, cost_drivers):
        try:
            a, b, c, d = self.coefficients[project_type]
        except KeyError:
            raise ValueError("Invalid project type selected")

        # 🔹 Convert all ratings to float multipliers
        eaf = 1.0
        for driver, rating in cost_drivers.items():
            try:
                eaf *= float(rating)   # ensure float multiplication
            except ValueError:
                raise ValueError(f"Invalid multiplier for {driver}: {rating}")

        effort = a * (kloc ** b) * eaf
        time = c * (effort ** d)
        staff = effort / time

        return {
            "Effort (PM)": round(effort, 2),
            "Development Time (Months)": round(time, 2),
            "Average Staff": round(staff, 2),
            "EAF": round(eaf, 3)

        }
