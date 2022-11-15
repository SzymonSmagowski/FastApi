import fastapi as fa
from typing import Optional,List
from pydantic import BaseModel


app = fa.FastAPI()

@app.post("/language/")
async def langauge(name: str = fa.Form(...), type: str = fa.Form(...)):
    return {"name": name, "type": type}