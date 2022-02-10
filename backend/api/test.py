from typing import Optional
from pydantic import BaseModel

class Test(BaseModel):
    u_region : str
    u_age : int
    u_policy_type : str