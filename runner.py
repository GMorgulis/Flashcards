import tkinter as tk
import subprocess
from flashcards import *

# Window setup
root = tk.Tk()
root.title("My Flashcards")
root.geometry("500x500")
root.state("zoomed")

# Title label
title_label = tk.Label(root, text="My Flashcards", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Scrollable frame setup
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)

scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((250, 0), window=scrollable_frame, anchor="n")
canvas.configure(yscrollcommand=scrollbar.set)

# Define global states for actions
minus_state = 0
edit_state = 0
rename_state = 0
buttons = []
flashcards = get_files("flashcard_sets")


# Button for creating a new set
plus_button = tk.Button(
    scrollable_frame, text="Create Set", font=("Arial", 16, "normal"), fg="white", bg="blue",
    width=20, height=2, command=lambda: on_plus_click()
)
plus_button.grid(row=0, column=0, pady=(10, 5), padx=10)

# Button for deleting a set
minus_button = tk.Button(
    scrollable_frame, text="Delete Set", font=("Arial", 16, "normal"), fg="white", bg="red",
    width=20, height=2, command=lambda: on_minus_click()
)
minus_button.grid(row=1, column=0, pady=(10, 5), padx=10)

# Button for editing a set
edit_button = tk.Button(
    scrollable_frame, text="Edit Set", font=("Arial", 16, "normal"), fg="white", bg="green",
    width=20, height=2, command=lambda: on_edit_click()
)
edit_button.grid(row=2, column=0, pady=(10, 5), padx=10)

# Button for renaming a set
rename_button = tk.Button(
    scrollable_frame, text="Rename Set", font=("Arial", 16, "normal"), fg="white", bg="orange",
    width=20, height=2, command=lambda: on_rename_click()
)
rename_button.grid(row=3, column=0, pady=(10, 5), padx=10)


# Callback functions
def on_rename_click():
    global rename_state
    rename_state = 1 - rename_state  # Toggle state


def on_edit_click():
    global edit_state
    edit_state = 1 - edit_state  # Toggle state


def on_flashcard_click(name):
    global minus_state, edit_state, rename_state

    if minus_state == 1:
        delete_set(name)
        minus_state = 0
        redraw_buttons()
    elif edit_state == 1:
        edit_state = 0
        subprocess.run(['python', 'egui.py', name, "1"])
    else:
        subprocess.run(['python', 'fgui.py', name])


def on_plus_click():
    popup = tk.Toplevel()
    popup.geometry("300x150")
    popup.title("Enter set name")

    label = tk.Label(popup, text="Enter set name:")
    label.pack(pady=10)

    entry = tk.Entry(popup)
    entry.pack(pady=10)

    def save_name():
        global name
        name = entry.get()  # Get the name from the entry widget
        popup.destroy()
        make_new_set(name)
        redraw_buttons()
        subprocess.run(['python', 'egui.py', name, "0"])

    submit_button = tk.Button(popup, text="Submit", command=save_name)
    submit_button.pack(pady=10)


def on_minus_click():
    global minus_state
    minus_state = 1


def redraw_buttons():
    global buttons
    # Destroy all previous buttons
    for button in buttons:
        button.destroy()
    buttons.clear()  # Clear the list of buttons
    create_buttons()


def create_buttons():
    global buttons
    flashcards = get_files("flashcard_sets")
    row = 0
    col = 1

    # Create buttons for each flashcard set
    for name in flashcards:
        btn = tk.Button(
            scrollable_frame, text=name, font=("Arial", 16, "normal"), bg="white",
            width=20, height=2, command=lambda n=name: on_flashcard_click(n)
        )
        btn.grid(row=row, column=col, pady=5, padx=10)
        buttons.append(btn)  # Store the button reference

        col += 1
        if col > 3:
            col = 1
            row += 1


create_buttons()

# Pack the scrollbar and canvas
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()
