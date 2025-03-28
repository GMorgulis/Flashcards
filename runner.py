from flashcards import*
import tkinter as tk
import subprocess

root = tk.Tk()
root.title("My Flashcards")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")


title_label = tk.Label(root, text="My Flashcards", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Create a frame and canvas for scrolling
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)

scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((250, 0), window=scrollable_frame, anchor="n")  
canvas.configure(yscrollcommand=scrollbar.set)

buttons = []
flashcards = get_files("flashcard_sets")

def on_flashcard_click(name):
    print(f"Opening flashcard: {name}")
    subprocess.run(['python', 'fgui.py', name])

def on_plus_click():
    make_new_set("pest")

plus_button = tk.Button(
    scrollable_frame, text="+", font=("Arial", 16, "normal"), fg="white", bg="blue",
    width=20, height=2, command=lambda: on_plus_click()
)
plus_button.grid(row=0, column=0, pady=(10, 5), padx=10)


minus_button = tk.Button(
    scrollable_frame, text="-", font=("Arial", 16, "normal"), fg="white", bg="red",
    width=20, height=2, command=lambda: print("Add new flashcard")
)
minus_button.grid(row=1, column=0, pady=(10, 5), padx=10)

def redraw_buttons():
    global buttons
    # Destroy all previous buttons
    for button in buttons:
        button.destroy()
    buttons.clear()  # Clear the list of buttons

    create_buttons()

def create_buttons():
    global buttons
    row = 0
    col = 1
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

# Pack scrollbar and canvas
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()
