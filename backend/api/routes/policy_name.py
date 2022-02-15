import sys
import os
from fastapi import APIRouter
from fastapi import Query

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from database import retrieve_policies, retrieve_all_policies

router = APIRouter()

@router.get("", response_description = "사용자의 정보에 해당하는 정책명 조회")
async def get_policy_name(u_region : str = Query(..., description = "사용자의 지역"),
                          u_age : int = Query(..., description = "사용자의 나이"),
                          policy_type : str = Query(..., description = "사용자가 선택한 정책 유형")):
    policies = await retrieve_policies(u_region, u_age, policy_type)
    if policies:
        return policies