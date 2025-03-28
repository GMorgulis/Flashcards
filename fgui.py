import tkinter as tk
from mylist import*
import csv


def create_list(filename):
    # Create an instance of the CircularLinkedList
    my_list = CircularLinkedList()
    
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        
        # Loop through each row in the CSV
        for row in reader:
            if len(row) != 2:
                continue  # Skip rows that don't have exactly 2 values
            val1 = row[0]
            val2 = row[1]
            my_list.add_node(val1, val2)
    
    return my_list

my_list = create_list("flashcard_sets/math.csv")
current_node = my_list.head
trial = current_node.val1

#breaks up the string so that it fits on the screen
def break_up(input_string):
    result = []
    i = 0
    while i < len(input_string):
        if i + 50 < len(input_string) and input_string[i + 50] != ' ':
            j = i + 50
            while j > i and input_string[j] != ' ':
                j -= 1
            if j == i: 
                result.append(input_string[i:i+50] + '—')
                i += 50
            else:
                result.append(input_string[i:j] + '\n')
                i = j + 1
        else:
            result.append(input_string[i:i+50] + '\n')
            i += 50

    return ''.join(result)



def on_btn1_click():
    print("btn1 is clicked")

def on_btn2_click():
    global trial, btn2
    if (trial == current_node.val1):
        trial = current_node.val2
    else:
        trial = current_node.val1
    
    btn2.destroy()
    btn2 = tk.Button(root, 
                 text=break_up(trial), 
                 width=50, 
                 height=15, 
                 font = ("Arial", 20),
                 command=lambda: on_btn2_click()
                 )
    btn2.grid(row=1, column=1, padx=5, pady=10, sticky="ew")


def on_btn3_click():
    print("btn3 is clicked")


root = tk.Tk()
root.geometry("500x200")  # Set window size

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
