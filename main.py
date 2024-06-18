from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


import uvicorn

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
