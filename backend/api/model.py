from typing import Optional
from pydantic import BaseModel
from pydantic import Field

def ResponseModel(data):
    return {
        "data" : [data]
    }