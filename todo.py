# Import modules
import sys
import datetime

# Create a text file to store tasks
todo_file = "todo.txt"

# Define a function to add a new task
def add_task(task):
    # Open the file in append mode
    with open(todo_file, "a") as f:
        # Write the task and the current date and time to the file
        f.write(f"{task} | {datetime.datetime.now()}\n")
        # Print a confirmation message
        print(f"Added task: {task}")

# Define a function to delete a task
def delete_task(number):
    # Open the file in read mode
    with open(todo_file, "r") as f:
        # Read all the lines from the file
        lines = f.readlines()
    # Check if the number is valid
    if 1 <= number <= len(lines):
        # Open the file in write mode
        with open(todo_file, "w") as f:
            # Loop through the lines
            for i, line in enumerate(lines):
                # Write the line to the file if it is not the one to be deleted
                if i != number - 1:
                    f.write(line)
        # Print a confirmation message
        print(f"Deleted task: {lines[number - 1].strip()}")
    else:
        # Print an error message
        print(f"Invalid task number: {number}")

# Define a function to complete a task
def complete_task(number):
    # Open the file in read mode
    with open(todo_file, "r") as f:
        # Read all the lines from the file
        lines = f.readlines()
    # Check if the number is valid
    if 1 <= number <= len(lines):
        # Open the file in write mode
        with open(todo_file, "w") as f:
            # Loop through the lines
            for i, line in enumerate(lines):
                # Write the line to the file with a "DONE" mark if it is the one to be completed
                if i == number - 1:
                    f.write(f"DONE {line}")
                else:
                    f.write(line)
        # Print a confirmation message
        print(f"Completed task: {lines[number - 1].strip()}")
    else:
        # Print an error message
        print(f"Invalid task number: {number}")

# Define a function to show the tasks
def show_tasks():
    # Open the file in read mode
    with open(todo_file, "r") as f:
        # Read all the lines from the file
        lines = f.readlines()
    # Check if the file is empty
    if lines:
        # Print the tasks with their numbers
        for i, line in enumerate(lines):
            print(f"[{i + 1}] {line.strip()}")
    else:
        # Print a message
        print("No tasks to show")

# Define a function to show the usage
def show_usage():
    # Print the usage instructions
    print("""Usage:
$ python todo.py add "task" # Add a new task
$ python todo.py del number # Delete a task
$ python todo.py done number # Complete a task
$ python todo.py show # Show the tasks
$ python todo.py help # Show the usage""")

# Check the number of command-line arguments
if len(sys.argv) > 1:
    # Get the command from the first argument
    command = sys.argv[1]
    # Check the command
    if command == "add":
        # Check if a task is given
        if len(sys.argv) > 2:
            # Get the task from the second argument
            task = sys.argv[2]
            # Call the add_task function
            add_task(task)
        else:
            # Print an error message
            print("No task given")
    elif command == "del":
        # Check if a number is given
        if len(sys.argv) > 2:
            # Get the number from the second argument
            number = int(sys.argv[2])
            # Call the delete_task function
            delete_task(number)
        else:
            # Print an error message
            print("No task number given")
    elif command == "done":
        # Check if a number is given
        if len(sys.argv) > 2:
            # Get the number from the second argument
            number = int(sys.argv[2])
            # Call the complete_task function
            complete_task(number)
        else:
            # Print an error message
            print("No task number given")
    elif command == "show":
        # Call the show_tasks function
        show_tasks()
    elif command == "help":
        # Call the show_usage function
        show_usage()
    else:
        # Print an error message
        print(f"Invalid command: {command}")
else:
    # Print an error message
    print("No command given")
