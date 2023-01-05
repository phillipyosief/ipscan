import tkinter as tk
import tkinter.filedialog

# Create the save button
def create_save_button(parent, log):
    def save():
        # Get the save file path
        save_path = tk.filedialog.asksaveasfilename()

        # Save the log text to the file
        with open(save_path, "w") as f:
            f.write(log.get("1.0", "end-1c"))

    save_button = tk.Button(parent, text="Save", command=save)
    return save_button
