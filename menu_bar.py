import tkinter as tk

def create_menu_bar(window):
    # Create the menu bar
    menu_bar = tk.Menu(window)

    # Create the File menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Create the Edit menu
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Undo")
    edit_menu.add_command(label="Redo")
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    # Create the About command
    def about():
        about_window = tk.Toplevel(window)
        about_window.title("About")
        about_label = tk.Label(about_window, text="Author: John Smith\nEmail: johnsmith@example.com\nWebsite: example.com")
        about_label.pack()
    menu_bar.add_command(label="About", command=about)

    # Add the menu bar to the window
    window.config(menu=menu_bar)
