import csv


class Node:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.next = None
        self.prev = None  # Add previous pointer

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, val1, val2):
        new_node = Node(val1, val2)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Points to itself (circular)
            new_node.prev = self.head  # Points to itself (circular)
        else:
            current = self.head.prev  # Last node (because it's circular)
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node  # Update head's previous pointer

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
            my_list.add_node(val1, val2)  # Already supports prev pointer
    
    return my_list