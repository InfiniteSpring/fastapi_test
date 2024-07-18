from typing import Annotated, List

from fastapi import APIRouter, Depends

from schemas import TaskAddSchema, TaskSchema, TaskIdSchema

from repository import TaskRepository


task_router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@task_router.post("")
async def add_task(
    task: Annotated[TaskAddSchema, Depends()],
) -> TaskIdSchema:
    task_id = await TaskRepository.add_one(task)
    # return TaskIdSchema(task_id=task_id)  ## that's right
    return {"ok": True, "task_id": task_id}   # that is working too


@task_router.get("")
async def get_tasks() -> list[TaskSchema]:
    all_tasks = await TaskRepository.find_all()
    return all_tasks
