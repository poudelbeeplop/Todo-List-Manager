# Todo-List-Manager
This is a simple command-line Todo List Manager that allows users to manage their tasks.

- **Add a task**
- **Remove a task**
- **Mark a task as completed**
- **List all tasks**


## Features

- **SQLite Database**: Tasks are stored in a local SQLite database (`todo_list.db`).
- **Command-Line Interface**: Users can interact with the todo list through command-line arguments.
- **Regular Expression Validation**: Task descriptions must not contain special characters, ensuring they are alphanumeric with spaces.

## Usage
python todo_list_manager.py -help or -h for help
python todo_list_manager.py -list or -l for list of task
python todo_list_manager.py -remove or r to remove a task
python todo_list_manager.py -complete or -c to mark task as copleted
