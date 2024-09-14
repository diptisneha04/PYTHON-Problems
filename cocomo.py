import tkinter as tk

def calculate_effort():
    try:
        kloc = float(entry_kloc.get())
        system_type = combo_system_type.get()

        # Constants for different system types
        if system_type == "Organic":
            a, b, c, d = float(entry_a.get()), float(entry_b.get()), float(entry_c.get()), float(entry_d.get())
        elif system_type == "Semi-Detached":
            a, b, c, d = float(entry_a.get()), float(entry_b.get()), float(entry_c.get()), float(entry_d.get())
        elif system_type == "Embedded":
            a, b, c, d = float(entry_a.get()), float(entry_b.get()), float(entry_c.get()), float(entry_d.get())
        else:
            raise ValueError("Invalid system type")

        effort = a * (kloc ** b)
        time = c * (effort ** d)
        personnel = effort / time

        label_result.config(text=f"Effort: {effort:.2f} person-months\nTime: {time:.2f} months\nPersonnel: {personnel:.2f} persons")
    except ValueError:
        label_result.config(text="Please enter valid input.")

# Create the main window
root = tk.Tk()
root.title("COCOMO Calculator")

# Widgets
label_kloc = tk.Label(root, text="Enter KLOC (Thousands of Lines of Code):")
entry_kloc = tk.Entry(root, font=("Arial", 14))  # Increased font size
label_system_type = tk.Label(root, text="Select System Type:")
combo_system_type = tk.StringVar(value="Organic")
combo_system_type_dropdown = tk.OptionMenu(root, combo_system_type, "Organic", "Semi-Detached", "Embedded")

# Constants input fields
label_a = tk.Label(root, text="Enter constant a:")
entry_a = tk.Entry(root, font=("Arial", 14))  # Increased font size
label_b = tk.Label(root, text="Enter constant b:")
entry_b = tk.Entry(root, font=("Arial", 14))  # Increased font size
label_c = tk.Label(root, text="Enter constant c:")
entry_c = tk.Entry(root, font=("Arial", 14))  # Increased font size
label_d = tk.Label(root, text="Enter constant d:")
entry_d = tk.Entry(root, font=("Arial", 14))  # Increased font size

button_calculate = tk.Button(root, text="Calculate", command=calculate_effort)
label_result = tk.Label(root, text="", font=("Arial", 14))  # Increased font size

# Layout
label_kloc.pack()
entry_kloc.pack()
label_system_type.pack()
combo_system_type_dropdown.pack()

# Constants layout
label_a.pack()
entry_a.pack()
label_b.pack()
entry_b.pack()
label_c.pack()
entry_c.pack()
label_d.pack()
entry_d.pack()

button_calculate.pack()
label_result.pack()

root.mainloop()
