import fastapi as fa

app = fa.FastAPI()

@app.get('/')
async def hello_world():
    return {"Hello":"World"}