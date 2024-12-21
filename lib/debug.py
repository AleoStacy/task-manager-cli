from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Task

engine = create_engine('sqlite:///task_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

# Test: Print all tasks in the database
tasks = session.query(Task).all()
for task in tasks:
    print(f"Task ID: {task.id}, Title: {task.title}, Completed: {task.completed}")
