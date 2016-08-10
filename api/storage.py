from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from datetime import datetime as dt

from models.base import Base
from models.task import Task


engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def create_task(param):
    data = {
        "name": param.get("name"),
        "remark": param.get("remark"),
        "deadline": dt.strptime(param.get("deadline"), "%Y-%m-%d"),
        "done": param.get("done")
    }
    new_task = Task(**data)
    session.add(new_task)
    session.commit()
    return new_task.id


def update_task(id, **kwargs):
    try:
        task = session.query(Task).filter(Task.id == id).one()
    except (MultipleResultsFound, NoResultFound):
        return False

    if kwargs["name"]:
        task.name = kwargs["name"]
    if kwargs["remark"]:
        task.remark = kwargs["remark"]
    if kwargs["deadline"]:
        task.deadline = kwargs["deadline"]
    if kwargs["done"]:
        task.done = kwargs["done"]

    session.add(task)
    session.commit()
    return True


def get_tasks(search=None):
    try:
        tasks = session.query(Task).all()
    except (NoResultFound):
        return None
    
    return tasks


def get_task(id):
    try:
        task = session.query(Task).filter(Task.id == id).one()
    except (MultipleResultsFound, NoResultFound):
        return None
    
    return task


def delete_task(id):
    task = session.query(Task).filter(Task.id == id).one()
    session.delete(task)
    session.commit()
    return True
