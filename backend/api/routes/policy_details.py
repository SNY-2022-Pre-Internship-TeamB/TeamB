import sys
import os
from fastapi import APIRouter
from fastapi import Query

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from database import retrieve_details, retrieve_all_details

router = APIRouter()

@router.get("", response_description = "모든 정책의 상세정보 조회")
async def get_all_policy_detail():
    details = await retrieve_all_details()
    if details:
        return details

@router.get("/{policy_name}", response_description = "해당하는 정책의 상세정보 조회")
async def get_policy_detail(policy_name : str = Query(..., description = "정책명")):
    details = await retrieve_details(policy_name)
    if details:
        return details