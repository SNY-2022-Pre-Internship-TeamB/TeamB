import sys
import os
from fastapi import APIRouter, Query, Path

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from database import *

router = APIRouter()

@router.get("", response_description = "해당하는 정책의 상세정보 조회")
async def get_policy_detail(policy_id : str = Path(..., description = "정책 번호")):
    details = await retrieve_details(policy_id)
    if details:
        return details