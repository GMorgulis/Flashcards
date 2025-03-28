import csv


class Node:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.next = None
        self.prev = None  

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, val1, val2):
        new_node = Node(val1, val2)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  
            new_node.prev = self.head  
        else:
            current = self.head.prev 
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node  

def create_list(filename):
    my_list = CircularLinkedList()
    
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if len(row) != 2:
                continue  # Skip rows that don't have exactly 2 values
            val1 = row[0]
            val2 = row[1]
            my_list.add_node(val1, val2) 
    
    return my_list