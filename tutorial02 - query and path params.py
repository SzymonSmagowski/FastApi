import fastapi as fa
from typing import Optional

app = fa.FastAPI()

@app.get('/')
async def hello_world():
    return {"Hello":"World"}

# annotations: typing is not required
@app.get('/component/{component_id}') # path parameter
async def get_component(component_id: int): #can specify type here
    return {"component_id": component_id}
# http://127.0.0.1:8000/component/1
# http://127.0.0.1:8000/docs - nice view

# query parameters:
@app.get('/component/') 
async def read_component(number: int, text: Optional[str]): #query parameter
    return {"number": number, "text": text}
# even if text is optional we still have to include it for example: &text= (nothing)