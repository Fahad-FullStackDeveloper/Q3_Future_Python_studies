from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from datetime import date
from typing import Optional, List

app = FastAPI()

# In-memory storage
USERS: dict[int, "User"] = {}
TASKS: dict[int, "Task"] = {}

# Auto-increment IDs
user_id_counter = 1
task_id_counter = 1

### 🧩 Pydantic Models ###

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr

class UserRead(UserCreate):
    id: int

class User(UserRead):
    pass  # For internal storage, same as UserRead in this case

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    user_id: int

    @validator("due_date")
    def due_date_must_be_future(cls, v):
        if v < date.today():
            raise ValueError("due_date must be today or later")
        return v

class Task(TaskCreate):
    id: int
    status: str = "pending"

    @validator("status")
    def validate_status(cls, v):
        allowed_statuses = ["pending", "in_progress", "completed"]
        if v not in allowed_statuses:
            raise ValueError(f"Status must be one of: {allowed_statuses}")
        return v


### 👤 User Endpoints ###

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    user_obj = User(id=user_id_counter, **user.dict())
    USERS[user_id_counter] = user_obj
    user_id_counter += 1
    return user_obj

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


### ✅ Task Endpoints ###

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    task_obj = Task(id=task_id_counter, **task.dict())
    TASKS[task_id_counter] = task_obj
    task_id_counter += 1
    return task_obj

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status: str):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if status not in ["pending", "in_progress", "completed"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    task.status = status
    return task

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return [task for task in TASKS.values() if task.user_id == user_id]
