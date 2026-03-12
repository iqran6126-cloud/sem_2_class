import os  # imports Python's built-in os module

def list_files_recursive(path):
    """
    This function prints all files and directories inside the given path.
    If it finds a directory, it calls itself again (recursion) to explore
    the contents of that directory.
    """

    # os.listdir(path) returns a list containing the names of files and directories
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            print("File:", full_path)

        elif os.path.isdir(full_path):
            print("Directory:", full_path)
            list_files_recursive(full_path)  # recursive call



list_files_recursive(".")