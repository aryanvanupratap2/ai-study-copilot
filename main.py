from fastapi import FastAPI
from pydantic import BaseModel
from graph import run_graph

app = FastAPI()

class Query(BaseModel):
    input: str

@app.post("/ask")
def ask(query: Query):
    return run_graph(query.input)