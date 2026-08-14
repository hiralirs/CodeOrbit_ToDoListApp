# To-Do List CLI App

A lightweight command-line Python application that helps you create, manage, and track your daily tasks with automatic file persistence.

## Features

* **View Tasks**: Displays a numbered list of all tasks with completion checkmarks (`[✓]` completed, `[ ]` pending).
* **Add Tasks**: Instantly append new tasks to your list.
* **Mark as Completed**: Interactively select and mark pending tasks as finished.
* **Remove Tasks**: Delete individual tasks by their list number.
* **Automatic Storage**: Saves and loads all task data automatically using a local `tasks.txt` file.

## Requirements

* Python 3.x (Uses standard libraries only—no external packages required)

## Usage

1. Open your terminal or command line prompt in the project directory.
2. Run the application:

```bash
python main.py
```
3. Choose options `1` through `5` from the interactive menu to manage your tasks.

## Data Format

Tasks are stored in `tasks.txt` using a pipe-delimited structure:
```text
Buy groceries|0
Submit project report|1
```
* `1` = Completed
* `0` = Pending
