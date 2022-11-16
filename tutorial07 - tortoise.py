import fastapi as fa
from typing import Optional,List
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from pydantic import BaseModel
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Todo(models.Model):
    
    id = fields.IntField(pk=True)
    todo = fields.CharField(max_length=250)
    due_date = fields.CharField(max_length=250)
    
    class PydanticMeta:
        pass
    
Todo_Pydantic = pydantic_model_creator(Todo, name="Todo")
TodoIn_Pydantic = pydantic_model_creator(Todo, name="TodoIn", exclude_readonly=True)

class Message(BaseModel):
    message: str

app = fa.FastAPI()

@app.get('/')
async def read_root():
    return {"Hello": "World"}

@app.post('/todo', response_model=Todo_Pydantic)
async def create(todo: TodoIn_Pydantic):
    obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_tortoise_orm(obj)

@app.get('/todo/{id}', response_model=Todo_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_one(id: int):
    return await Todo_Pydantic.from_queryset_single(Todo.get(id=id))

@app.put("/todo/{id}", response_model=Todo_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update(id: int, todo: TodoIn_Pydantic):
    await Todo.filter(id=id).update(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_queryset_single(Todo.get(id=id))

@app.delete("/todo/{id}", response_model=Message, responses={404: {"model": HTTPNotFoundError}})
async def delete(id: int):
    delete_obj = await Todo.filter(id=id).delete()
    if not delete_obj:
        raise fa.HTTPException(status_code=404, detail="This todo is not found.")
    return Message(message="Succesfully Deleted")

register_tortoise(
    app,
    db_url="sqlite://store.db",
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)