from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Task

engine = create_engine('sqlite:///task_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_db():
    tasks = [
        Task(title="Learn Python", description="Complete Python course", completed=False),
        Task(title="Build CLI", description="Build a task manager CLI", completed=False)
    ]
    session.add_all(tasks)
    session.commit()
    session.close()  # Ensure session is closed after committing

if __name__ == "__main__":
    seed_db()
    print("Database seeded!")
