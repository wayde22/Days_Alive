import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Label, Button, Frame
from datetime import datetime


def calculate_days_alive():
    try:
        # Get the current date
        current_date = datetime.now()

        # Get the user input
        year_of_birth = int(year_entry.get())
        month_of_birth = int(month_entry.get())
        day_of_birth = int(day_entry.get())

        # Create a datetime object for the user's birthdate
        birth_date = datetime(year_of_birth, month_of_birth, day_of_birth)

        # Calculate the difference in days
        days_alive = (current_date - birth_date).days

        # Display the results
        result_label.config(text=f"You have been alive for {days_alive} days.")
    except ValueError:
        result_label.config(text="Please enter valid date values.")


# Set up the main application window
root = tk.Tk()
root.title("Days Alive Calculator")
style = Style(theme='flatly')  # You can choose different themes like 'cosmo', 'flatly', 'minty', etc.
root.geometry('400x300')

# Create a frame for input fields and buttons
frame = Frame(root, padding="20")
frame.pack(fill='both', expand=True)

# Add input fields
Label(frame, text="Year of Birth:").grid(row=0, column=0, padx=10, pady=10)
year_entry = Entry(frame)
year_entry.grid(row=0, column=1, padx=10, pady=10)

Label(frame, text="Month of Birth:").grid(row=1, column=0, padx=10, pady=10)
month_entry = Entry(frame)
month_entry.grid(row=1, column=1, padx=10, pady=10)

Label(frame, text="Day of Birth:").grid(row=2, column=0, padx=10, pady=10)
day_entry = Entry(frame)
day_entry.grid(row=2, column=1, padx=10, pady=10)

# Add a button to calculate days alive
calculate_button = Button(frame, text="Calculate Days Alive", command=calculate_days_alive)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Add a label to display the result
result_label = Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
