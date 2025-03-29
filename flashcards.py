import os

'''Some libary metods for flashcards. Not all of them are currently in use'''

def get_home_path():
    return "flashcard_sets"

def dir_exists(path):
    """Returns True if directory exists, False otherwise."""
    return os.path.isdir(path)

def file_exists(path):
    """Checks if a file exists at the given path."""
    return os.path.isfile(path)

def home_checker():
    """Checks if the home directory for flashcards exists, otherwise creates it."""
    if not dir_exists(get_home_path()):
        os.makedirs(get_home_path(), 0o777)

def make_new_set(name):
    """Creates a new card set."""
    path = os.path.join(get_home_path(), f"{name}.csv")
    
    if dir_exists(path):
        print(f"Error: set '{name}' already exists")
        return -1

    print(f"Path: {path}")
    with open(path, 'w'):
        pass  # Create an empty file
    return 0

def add_to_set(set_name, key, value):
    """Checks if the flashcards set exists, adds key, value pair."""
    path = os.path.join(get_home_path(), f"{set_name}.csv")
    
    try:
        with open(path, 'a') as file:
            file.write(f"{key}, {value}\n")
        return 0
    except FileNotFoundError:
        return -1

def remove_from_set(set_name, num):
    """Removes flashcards with the given number from the set."""
    src = os.path.join(get_home_path(), f"{set_name}.csv")
    dest = os.path.join(get_home_path(), "txzf123.csv")
    
    try:
        with open(src, 'r') as src_file, open(dest, 'w') as dest_file:
            count = 0
            for line in src_file:
                if count != num:
                    dest_file.write(line)
                count += 1
        os.remove(src)
        os.rename(dest, src)
        return 0
    except FileNotFoundError:
        print("Error: Could not open the source file")
        return -1

def delete_set(set_name):
    """Removes a set of flashcards."""
    src = os.path.join(get_home_path(), f"{set_name}")
    try:
        os.remove(src)
        return 0
    except FileNotFoundError:
        return -1

def get_files(directory):
    file_names = []
    for entry in os.listdir(directory):
        # Only add files, skip directories (and '.' or '..' entries)
        if os.path.isfile(os.path.join(directory, entry)):
            file_names.append(entry)
    return file_names


