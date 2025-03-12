import click
import datetime
from mongoengine import connect,Document, StringField, SequenceField, DateTimeField
import humanize
import os


mongodb_uri = os.getenv("MONGODB_URI") or "mongodb://localhost:27017/tasks"
connect(host=mongodb_uri)

class Task(Document):
    id = SequenceField(primary_key=True)
    description = StringField(required=True, max_length=500)
    status = StringField(choices=["todo", "in-progress", "done"], default="todo")
    createdAt = DateTimeField(default=datetime.datetime.now(datetime.UTC))
    updatedAt = DateTimeField(null=True)


    def __str__(self):
        status_icons = {
            "in-progress": "🚀",
            "done": "✅",
            "todo": "📝"
        }

        logo = status_icons.get(self.status)
        time_ago = humanize.naturaltime(datetime.datetime.now() - self.createdAt)

        return f"{logo}  [Task ID: {self.id}]  {self.description}\n   Status: {self.status.upper()}  |   Created: {time_ago} ago \n"



@click.group(help="Task Manager CLI - Manage your tasks easily")
def cli():
    pass

@click.command(help="Add a new task to the list")
@click.argument("desc", required=False)
def add(desc):
    try:
        while not desc:
            click.secho("Enter the task name:", fg="blue")
            desc = input(">> ").strip()
        task = Task(description=desc)
        task.save()
        click.secho(f"Task added successfully (ID:{task.id}) 🎉",fg="green")
    except Exception as e:
        click.secho(f"Something went wrong! {e}", fg="red")

@click.command(help="Update an existing task")
@click.argument("task_id", required = False)
@click.argument("desc", required = False)
def update(task_id, desc):
    try:
        while not task_id:
            click.secho("Enter the Task ID to update", fg="blue")
            task_id = input(">> ").strip()
        if not task_id.isdigit():
            click.secho(f"Invalid task id", fg="red")
            return
        task_id = int(task_id)
        task = Task.objects(id =task_id).first()
        if not task:
            click.secho(f"No task with id {task_id} found", fg="red")
            return
        while not desc:
            click.secho("Enter task name", fg="blue")
            desc = input(">> ").strip()
        task.description = desc
        task.updatedAt = datetime.datetime.now()
        task.save()
        click.secho(f"Task updated successfully (ID:{task.id}) 🎉", fg="green")
    except Exception as e:
        click.secho(f"Something went wrong! {e}",fg="red")

@click.command(help="Delete a task by ID")
@click.argument("task_id", required = False)
def delete(task_id):
    try:
        while not task_id:
            click.secho("Enter the Task ID to update", fg="blue")
            task_id = input(">> ").strip()
        if not task_id.isdigit():
            click.secho(f"Invalid task id", fg="red")
            return
        task_id = int(task_id)
        task = Task.objects(id=task_id).first()
        if not task:
            click.secho(f"No task with id {task_id} found", fg="red")
            return
        task.delete()
        click.secho(f"Task deleted successfully (ID:{task.id}) 🎉", fg="green")
    except Exception as e:
        click.secho(f"Something went wrong! {e}",fg="red")

@click.command(help="Mark a task as 'In Progress'")
@click.argument("task_id", required = False)
def mark_in_progress(task_id):
    try:
        while not task_id:
            click.secho("Enter the Task ID to update", fg="blue")
            task_id = input(">> ").strip()
        if not task_id.isdigit():
            click.secho(f"Invalid task id", fg="red")
            return
        task_id = int(task_id)
        task = Task.objects(id=task_id).first()
        if not task:
            click.secho(f"No task with id {task_id} found", fg="red")
            return
        task.status = "in-progress"
        task.save()
        click.secho(f"{task.description} is in progress", fg="green")
    except Exception as e:
        click.secho(f"Something went wrong! {e}", fg="red")

@click.command(help="Mark a task as 'Done'")
@click.argument("task_id", required = False)
def mark_done(task_id):
    try:
        while not task_id:
            click.secho("Enter the Task ID to update", fg="blue")
            task_id = input(">> ").strip()
        if not task_id.isdigit():
            click.secho(f"Invalid task id", fg="red")
            return
        task_id = int(task_id)
        task = Task.objects(id=task_id).first()
        if not task:
            click.secho(f"No task with id {task_id} found", fg="red")
            return
        task.status = "done"
        task.save()
        click.secho(f"'{task.description}' has been completed 🎉", fg="green")
    except Exception as e:
        click.secho(f"Something went wrong! {e}", fg="red")

@click.command(help="List all tasks")
@click.argument("status", required = False)
def list(status):
    try:
      if status:
        status = status.lower()

        valid_statuses = {"todo", "in-progress", "done"}

        if status not in valid_statuses:
          click.secho("Invalid status parameter. Use 'todo', 'in-progress', or 'done'.", fg="red")
          return

      if status:
        tasks = Task.objects(status = status)
      else:
        tasks = Task.objects()

      if not tasks:
          click.secho("No tasks available", fg="blue")
      else:
          for task in tasks:
              click.secho(str(task))

    except Exception as e:
        click.secho(f"Something went wrong! {e}", fg="red")


cli.add_command(add)
cli.add_command(update)
cli.add_command(delete)
cli.add_command(mark_in_progress, "mark-in-progress")
cli.add_command(mark_done, "mark-done")
cli.add_command(list)



if __name__ == "__main__":
    cli()