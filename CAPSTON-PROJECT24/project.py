import datetime

# Function to read user credentials from user.txt
def read_user_credentials():
    user_credentials = {}
    with open("user.txt", "r") as user_file:
        for line in user_file:
            username, password = line.strip().split(", ")
            user_credentials[username] = password
    return user_credentials

# Function to authenticate users
def authenticate_user():
    user_credentials = read_user_credentials()

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in user_credentials and user_credentials[username] == password:
            print("Login successful!\n")
            return username
        else:
            print("Invalid username or password. Please try again.\n")

# Function to register a new user
def register_user():
    if current_user != 'admin':
        print("Only the 'admin' user can register new users.\n")
        return

    new_username = input("Enter the new username: ")
    new_password = input("Enter the password for the new user: ")
    confirm_password = input("Confirm the password: ")

    if new_password == confirm_password:
        with open("user.txt", "a") as user_file:
            user_file.write(f"{new_username}, {new_password}\n")
        print("User registered successfully!\n")
    else:
        print("Passwords do not match. User registration failed.\n")

# Function to add a new task
def add_task():
    assigned_user = input("Enter the username of the person the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter a description of the task: ")
    due_date = input("Enter the due date for the task (YYYY-MM-DD): ")

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    completed_status = "No"

    with open("tasks.txt", "a") as tasks_file:
        tasks_file.write(
            f"{assigned_user}, {task_title}, {task_description}, {current_date}, {due_date}, {completed_status}\n"
        )

    print("Task added successfully!\n")

# Function to view all tasks
def view_all_tasks():
    with open("tasks.txt", "r") as tasks_file:
        for task in tasks_file:
            print(task.strip())

# Function to view tasks assigned to the current user
def view_my_tasks():
    with open("tasks.txt", "r") as tasks_file:
        for task in tasks_file:
            if task.startswith(f"{current_user},"):
                print(task.strip())

# Function to display statistics for the admin user
def display_statistics():
    if current_user != 'admin':
        print("Only the 'admin' user can view statistics.\n")
        return

    total_tasks = 0
    total_users = 0

    with open("tasks.txt", "r") as tasks_file:
        total_tasks = sum(1 for _ in tasks_file)

    with open("user.txt", "r") as user_file:
        total_users = sum(1 for _ in user_file)

    print(f"Total number of tasks: {total_tasks}")
    print(f"Total number of users: {total_users}\n")

# Main program execution
current_user = authenticate_user()

while True:
    print("Menu:")
    print("a - Add a new task")
    print("va - View all tasks")
    print("vm - View my tasks")
    print("r - Register a new user")
    if current_user == 'admin':
        print("ds - Display statistics")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == "a":
        add_task()
    elif choice == "va":
        view_all_tasks()
    elif choice == "vm":
        view_my_tasks()
    elif choice == "r":
        register_user()
    elif current_user == 'admin' and choice == "ds":
        display_statistics()
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
