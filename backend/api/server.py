from fastapi import FastAPI
from model import *

app = FastAPI()

@app.get("/")
def test_func():
    return "Test Func"

@app.post("/nums/")
async def policy_num(item : policy_name):
    test_dict = item.dict()
    if item.u_region == "서울":
        test_dict.update({"정책 번호" : "R0001"})
    if item.u_region == "기타":
        test_dict.update({"정책 번호": "R0002"})
    return test_dict