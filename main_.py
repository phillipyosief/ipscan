import tkinter as tk

from ui import log_frame
from ui import input_fields
from ui import save_button
from ui import dark_mode
from ui import menu_bar

# Create the main window
window = tk.Tk()
window.title("My Tkinter App")

# Create the heading
heading = tk.Label(window, text="IP Range Scanner", font=("Helvetica", 18))
heading.pack()

# Create the log frame
log_frame, log = log_frame.create_log_frame(window)

# Create the menu bar
menu_bar.create_menu_bar(window)

# Create the dark mode toggle button
toggle_button = dark_mode.create_dark_mode_toggle(window, heading, log_frame, input_field_1, input_field_2, start_button, save_button)

# Create the input fields and start button
input_field_1, input_field_2, start_button = input_fields.create_input_fields(window)

# Create the save button
save_button = save_button.create_save_button(window, log)

# Run the main loop
window.mainloop()
