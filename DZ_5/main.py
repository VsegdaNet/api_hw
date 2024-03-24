from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool

tasks = {
    1: Task(id=1, title="Задача 1", description="Описание задачи 1", status=False),
    2: Task(id=2, title="Задача 2", description="Описание задачи 2", status=True),
}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return list(tasks.values())

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return tasks[task_id]

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    max_id = max(tasks.keys(), default=0)
    new_id = max_id + 1
    tasks[new_id] = task
    return tasks[new_id]

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    tasks[task_id] = task
    return tasks[task_id]

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return tasks.pop(task_id)