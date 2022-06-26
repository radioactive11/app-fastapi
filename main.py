from fastapi import FastAPI

app = FastAPI()


@app.get("/touch")
def touch():
    return {"hello": "world :)"}

