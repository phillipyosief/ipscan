import tkinter as tk

# Create the log frame and log text widget
def create_log_frame(parent):
    log_frame = tk.Frame(parent)
    log = tk.Text(log_frame, state="disabled")
    log.pack(fill="both", expand=True)
    log_frame.pack(fill="both", expand=True)
    return log_frame, log
