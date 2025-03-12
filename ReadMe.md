# Task Tracker CLI

## Overview
Task Tracker is a command-line interface (CLI) application that allows users to manage their tasks efficiently. It supports adding, updating, deleting, and tracking the progress of tasks.


## Project URL
[Task Tracker Project](https://roadmap.sh/projects/task-tracker)

## Features
- Add, update, and delete tasks
- Mark tasks as in progress or done
- List all tasks
- Filter tasks by status (done, not done, in progress)
- Stores tasks in MongoDB

## Prerequisites
Before setting up the project, ensure you have the following installed:

- **Python** (Recommended: Python 3.10+)
- **MongoDB** 

## Installation and Setup
Follow these steps to set up and run the Task Tracker CLI:
## Setup Instructions

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB Connection**
   - Create a `.env` file in the project directory.
   - Add your MongoDB connection string:
     ```sh
     MONGO_URI=mongodb://localhost:27017/task_tracker
     ```
   - Ensure MongoDB is running locally or provide a cloud-based connection string.

5. **Install the CLI as a Package**
   ```sh
   pip install .
   ```

6. **Run the CLI**
   ```sh
   task-cli --help
   ```

## Implementation Details
- **Click Library:** This project uses `Click` to handle command-line arguments and commands. Click makes it easier to build user-friendly CLI applications.
- **Setup File:** The project includes a `setup.py` file, allowing it to be installed as a package. This makes it possible to run commands globally after installation.
- **MongoDB Storage:** Tasks are stored in a mongodb database.

## Example Commands
Add a task:
```sh
task-cli add "Finish the report" 
```

List all tasks:
```sh
task-cli list
```

Mark a task as done:
```sh
task-cli mark-done 1
```

For more details, run:
```sh
task-cli --help
