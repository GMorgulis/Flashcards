import sys
import tkinter as tk

# Ensure correct usage
if len(sys.argv) != 2:
    print("Usage: python script.py <argument>")
    sys.exit(1)

folder = "flashcard_sets/"
argument = sys.argv[1]
ending = ".csv"
fullpath = folder + argument + ending

def save_to_file():
    """Writes the content of the text box to the specified file."""
    content = text_box.get("1.0", tk.END).strip()  # Get all text
    with open(fullpath, "w", encoding="utf-8") as file:
        file.write(content)

def on_return():
    """Closes the window when the 'Done' button is clicked."""
    root.destroy()

# Create the GUI window
root = tk.Tk()
root.title("Large Input Box")
root.geometry("500x500")
root.state("zoomed")


# Create a frame to hold the text box and scrollbar
frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Create a large text box
text_box = tk.Text(frame, wrap="word", font=("Arial", 14), yscrollcommand=scrollbar.set)
text_box.pack(expand=True, fill="both")

# Link scrollbar to text box
scrollbar.config(command=text_box.yview)

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Submit button (Green)
submit_button = tk.Button(button_frame, text="Submit", command=save_to_file, font=("Arial", 14), bg="green", fg="white")
submit_button.pack(side="left", padx=10)

# Return button (Blue)
done_button = tk.Button(button_frame, text="Return", command=on_return, font=("Arial", 14), bg="purple", fg="white")
done_button.pack(side="left", padx=10)

root.mainloop()
