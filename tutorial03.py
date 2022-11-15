import fastapi as fa
from typing import Optional
from pydantic import BaseModel

class Package(BaseModel):
    name:str
    number: str
    description: Optional[str] = None

app = fa.FastAPI()

@app.get('/')
async def hello_world():
    return {"Hello":"World"}

@app.post('/package/{priority}')
async def make_package(priority:int,package: Package,value:bool):
    return {"priority":priority,**package.dict(),"value":value}