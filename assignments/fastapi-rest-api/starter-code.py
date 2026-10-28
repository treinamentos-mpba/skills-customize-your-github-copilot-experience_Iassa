from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field
import uvicorn


app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)