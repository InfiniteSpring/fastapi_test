from database import new_session, TasksORM
from schemas import TaskAddSchema, TaskSchema
from sqlalchemy import select

from database import TasksORM


class TaskRepository:

    @classmethod
    async def add_one(
            cls, data: TaskAddSchema
    ) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksORM(**task_dict)
            session.add(task)
            await session.flush()   # to get task.id
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TasksORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
