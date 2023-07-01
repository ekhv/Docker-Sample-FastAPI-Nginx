from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root() -> dict:
    return {"msg": "Hello, World!"}
