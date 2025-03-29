import tkinter as tk
from mylist import*
from helper import *
import sys

''' Creates the GUI for actually using the flashcards for studyings'''

if len(sys.argv) != 2:
    print("Usage: python script.py <argument>")
    sys.exit(1)

folder = "flashcard_sets/"
argument = sys.argv[1]

my_list = create_list(folder + argument)
current_node = my_list.head
trial = current_node.val1

def update_button():
    global btn2
    btn2.destroy()
    btn2 = tk.Button(root, 
                 text=break_up(trial), 
                 width=50, 
                 height=15, 
                 font = ("Arial", 20),
                 command=lambda: on_btn2_click()
                 )
    btn2.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

#click prev button
def on_btn1_click():
    global current_node, btn2, trial
    current_node = current_node.prev
    trial = current_node.val1
    update_button()

#click flashcard button
def on_btn2_click():
    global trial, btn2
    if (trial == current_node.val1):
        trial = current_node.val2
    else:
        trial = current_node.val1
    
    btn2.destroy()
    update_button()

# click new button
def on_btn3_click():
    global current_node, btn2, trial
    current_node = current_node.next
    trial = current_node.val1
    update_button()

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("500x500")
root.state("zoomed")


root.rowconfigure(0, weight=0)  
root.rowconfigure(1, weight=0)  
root.columnconfigure(0, weight=1, minsize=50)  
root.columnconfigure(1, weight=0, minsize=200)  
root.columnconfigure(2, weight=1, minsize=50) 

# Create label at the top
label = tk.Label(root, text="Flashcards", font=("Arial", 30, "bold"))
label.grid(row=0, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

# Create buttons with fixed widths
btn1 = tk.Button(root,
                  text="Prev",
                  width=10, 
                  height=2, 
                  bg="blue", 
                  fg="white",
                  font = ("Arial", 15),
                  command=lambda: on_btn1_click()
                  )
btn1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

btn2 = tk.Button(root, 
                 text=break_up(trial), 
                 width=50, 
                 height=15, 
                 font = ("Arial", 20),
                 command=lambda: on_btn2_click()
                 )
 
btn2.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

btn3 = tk.Button(root, 
                 text="Next", 
                 width=10, 
                 height=2, 
                 bg="blue", 
                 fg="white",
                 font = ("Arial", 15),
                 command=lambda: on_btn3_click()
                 )
btn3.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

root.mainloop()
