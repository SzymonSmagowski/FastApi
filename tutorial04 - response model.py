import fastapi as fa
from typing import Optional
from pydantic import BaseModel

class PackageIn(BaseModel):
    secret_id: int
    name: str
    number: str
    description: Optional[str] = None

class Package(BaseModel):
    name:str
    number: str
    description: Optional[str] = None

app = fa.FastAPI()

@app.get('/')
async def hello_world():
    return {"Hello":"World"}

@app.post("/package/", response_model=Package, response_model_include={"description"}) # response_model_exclude is done to exclude certain fields
async def make_package(package: PackageIn):
    return package