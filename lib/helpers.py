from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Task

# Database Setup
engine = create_engine('sqlite:///task_manager.db')
Session = sessionmaker(bind=engine)

def add_task(title, description):
    session = Session()
    task = Task(title=title, description=description)
    session.add(task)
    session.commit()
    print(f"Task '{title}' added successfully.")
    session.close()

def list_tasks():
    session = Session()
    tasks = session.query(Task).all()
    if tasks:
        for task in tasks:
            print(f"{task.id}: {task.title} - {'Completed' if task.completed else 'Not completed'}")
    else:
        print("No tasks available.")
    session.close()

def complete_task(task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.completed = True
        session.commit()
        print(f"Task '{task.title}' marked as completed.")
    else:
        print("Task not found.")
    session.close()

def delete_task(task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task '{task.title}' deleted successfully.")
    else:
        print("Task not found.")
    session.close()
