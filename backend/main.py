from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test_func():
    return "Test Func"