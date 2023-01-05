import tkinter as tk

# Create the input fields and start button
def create_input_fields(parent):
    # Create the input fields and start button
    input_field_1 = tk.Entry(parent)
    input_field_2 = tk.Entry(parent)
    start_button = tk.Button(parent, text="Start")
    return input_field_1, input_field_2, start_button
