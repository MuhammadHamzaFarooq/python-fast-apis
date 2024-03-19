from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_wrold():
    return {"message":"Hello World"}