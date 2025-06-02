from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class TaskBase(BaseModel):
    title: str
    completed: bool = False

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

def to_camel(string: str) -> str:
    words = string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])