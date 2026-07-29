# Task Manager

A simple, colorful CLI task/todo manager built with Python. Uses JSON to persist data and ANSI color codes to highlight priorities.

## Features
- Add tasks with title, priority (high/medium/low), and optional due date
- List all tasks with priority color coding
- Mark tasks as complete
- Delete tasks
- Filter by priority or status
- Data persisted automatically to `tasks.json`

## Technologies
- Python 3
- JSON for storage

## Installation
1. Clone this repository or download the source files.
2. Ensure you have Python installed.
3. Run the script directly. No additional dependencies are required!

## Usage
Run the main script:
```bash
python main.py
```

### Examples
When you run the app, you will see a menu:
```
--- 📝 TASK MANAGER ---
1. Add Task
2. List All Tasks
3. Mark Task Completed
4. Delete Task
5. Filter Tasks
6. Exit
```

**Adding a Task:**
- Choose option `1`.
- Enter the task title: `Buy groceries`
- Enter the priority: `high`
- Enter a due date (optional): `Tomorrow`

**Listing Tasks:**
- Choose option `2`.
- The CLI will print out your tasks. High priority tasks will be displayed in red, medium in yellow, and low in green.

## Project Structure
- `main.py` - The main CLI application loop and user interaction.
- `task.py` - Contains the `TaskManager` class and handles all JSON storage.
- `tasks.json` - Generated automatically to save your tasks.
