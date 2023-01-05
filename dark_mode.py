import tkinter as tk

# Set the default colors for light mode
light_bg = "#ffffff"
light_fg = "#000000"

# Set the default colors for dark mode
dark_bg = "#000000"
dark_fg = "#ffffff"

# Create a flag to track the current mode
is_dark_mode = False

# Create the toggle mode button
def create_dark_mode_toggle(window, heading, log_frame, input_field_1, input_field_2, start_button, save_button):
    toggle_button = tk.Button(window, text="Dark Mode", command=lambda: toggle_mode(window, heading, log_frame, input_field_1, input_field_2, start_button, save_button))
    return toggle_button

# Create the toggle mode button
def toggle_mode(window, heading, log_frame, input_field_1, input_field_2, start_button, save_button):
    global is_dark_mode
    global light_bg
    global light_fg
    global dark_bg
    global dark_fg
    if is_dark_mode:
        # Set the colors to light mode
        window.config(bg=light_bg)
        heading.config(fg=light_fg)
        log_frame.config(fg=light_fg, bg=light_bg)
        input_field_1.config(fg=light_fg, bg=light_bg)
        input_field_2.config(fg=light_fg, bg=light_bg)
        start_button.config(fg=light_fg, bg=light_bg)
        save_button.config(fg=light_fg, bg=light_bg)
        toggle_button.config(text="Dark Mode")
        is_dark_mode = False
    else:
        # Set the colors to dark mode
        window.config(bg=dark_bg)
        heading.config(fg=dark_fg)
        log_frame.config(fg=dark_fg, bg=dark_bg)
        input_field_1.config(fg=dark_fg, bg=dark_bg)
        input_field_2.config(fg=dark_fg, bg=dark_bg)
        start_button.config(fg=dark_fg, bg=dark_bg)
        save_button.config(fg=dark_fg, bg=dark_bg)
        toggle_button.config(text="Light Mode")
        is_dark_mode = True


