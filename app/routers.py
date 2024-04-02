from fastapi import APIRouter, Request
from schemas import TaskCreateSchema
from models import TaskModel
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import select, insert

tasks_router = APIRouter(prefix='/api/tasks')

""" 
@tasks_router.post(path='/create/')# full path = /api/v1/tasks/create/
def create_task_point(request: Request, task: TaskCreateSchema):
    new_task = TaskModel(
        title=task.title,
        description=task.description,
    )
    session = Session(engine) # <- создаю сессию с БД
    session.add(new_task) # <- записывает обьект в БД
    session.commit() # <- делает сохрание
    session.close() # <- закрывает сессию
    return {"task": task}

@tasks_router.get('/list/')
def list_tasks_point(request:Request):
    session = Session(engine)
    stmt = select(TaskModel)
    print(stmt)
    """
"""     SELECT tasks_table.id, tasks_table.title, tasks_table.description, tasks_table.status     
    FROM tasks_table
    """ """
    tasks:list = session.scalars(stmt).all()
    return tasks

 """
@tasks_router.get('/list/')
def get_list_task(request: Request):
    session = Session(engine)
    stmt = select(TaskModel)
    object_db = session.execute(stmt)
    tasks:list = object_db.scalars().all()
    session.close()
    return tasks

@tasks_router.post('/create/')
def create_task(request: Request, task: TaskCreateSchema):
    session = Session(engine)
    stmt = insert(TaskModel).values(title=task.title, description=task.description)
    session.execute(stmt)
    session.commit()
    session.close()
    return task

@tasks_router.put('/list/')
def update_task(request: Request, task_id: int, task_change: TaskCreateSchema):
    session = Session(engine)
    stmt = select(TaskModel).where(TaskModel.id==task_id)
    object_db = session.execute(stmt)
    print(object_db)
    task = object_db.scalars().first()
    task.title = task_change.title
    task.description = task_change.description
    task.status = task_change.status
    session.merge(task)
    session.commit()
    session.close()
    return task

@tasks_router.delete('/list/')
def delete_task(request: Request, task_id: int):
    session = Session(engine)
    stmt = select(TaskModel).where(TaskModel.id==task_id)
    object_db = session.execute(stmt)
    task = object_db.scalar()
    session.delete(task)
    session.commit()
    session.close()
    return {"massage": f"task id: {task_id} delete"}