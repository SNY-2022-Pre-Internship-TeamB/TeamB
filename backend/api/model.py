from typing import Optional
from pydantic import BaseModel

class policy_name(BaseModel):
    u_region : str
    u_age : int
    u_policy_type : str

class policy_detail(BaseModel):
    policy_id : str
