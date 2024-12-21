# Task Manager CLI

A simple command-line interface (CLI) application for managing tasks, built with Python, SQLAlchemy, and SQLite. This project allows users to add, list, complete, and delete tasks from a database.

# Features
- Add a new task: Allows users to add tasks with titles and descriptions.
- List all tasks: Displays all tasks stored in the database, showing whether they are completed or not.
- Complete a task: Marks a task as completed.
- Delete a task: Deletes a task from the database.
- Persistent storage: All data is stored in an SQLite   database, allowing data to persist across sessions.

# Technologies Used
- Python 3.x: Programming language used to build the application.
- SQLAlchemy: ORM (Object-Relational Mapper) used for database operations.
- SQLite: A lightweight, disk-based database that doesn't require a separate server process.
- CLI (Command-Line Interface): A simple interface to interact with the application.

# Installation

Prerequisites
- Python 3.x installed on your system.
- pip (Python package installer) for managing dependencies.

# Steps to install

step 1: clone the repository

git clone https://github.com/AleoStacy/task-manager-cli.git
cd task-manager-cli

step 2: install

python3 -m venv venv
source venv/bin/activate  

step 3: Install the required dependencies:

pip install -r requirements.txt

step 4: Initialize the database and seed with sample data (this step is optional but recommended):

python seed.py

# Usage
Running the Task Manager CLI
After setting up the project, you can start using the task manager CLI.

1. Start the task manager:
    python cli.py

2. You'll see a menu with the following options:

  Choose an option:
1. Add a new task
2. List all tasks
3. Complete a task
4. Delete a task
5. Exit

3. Choose an option by entering the corresponding number (1-5).

  Option 1: Add a new task by entering a title and description.
  Option 2: View all tasks and their status.
  Option 3: Mark a task as completed by entering the task ID.
  Option 4: Delete a task by entering the task ID.
  Option 5: Exit the application.

# Database
- The application uses SQLite (task_manager.db) to store tasks persistently.
- The database is automatically created when you first run the application or use the seed.py script.
- You can view and modify the tasks directly in the SQLite database file if needed.

# Project Structure

task-manager-cli/
│
├── db/
│   └── models.py       # SQLAlchemy models (Task)
│
├── lib/
│   ├── helpers.py      # Functions for adding, listing, completing, and deleting tasks
│   ├── cli.py          # Command-line interface for interacting with the app
│   └── seed.py         # Script to seed the database with initial tasks
│
├── requirements.txt    # List of project dependencies
└── README.md           # Project documentation


# How to Contribute
1. Fork the repository.
2. Create a new branch (git checkout -b feature-name).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push to your branch (git push origin feature-name).
Open a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

