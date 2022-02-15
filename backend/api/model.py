from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse

class PolicySchema(BaseModel):
    p_name: str = Field()
    policy_id: str = Field()
    introduction: str = Field()
    policy_type: str = Field()
    support: str = Field()
    operating_period: str = Field()
    application_period: str = Field()
    scale: str = Field()
    p_region: str = Field()
    p_age_max: str = Field()
    p_age: str = Field()
    p_region_income: str = Field()
    p_education: str = Field()
    p_major1: str = Field()
    p_employment: str = Field()
    p_major2: str = Field()
    detail: str = Field()
    restriction: str = Field()
    procedure: str = Field()
    announcement: str = Field()
    m_site: str = Field()
    document: str = Field()
    etc: str = Field()
    a_name: str = Field()
    m_name: str = Field()
    a_site1: str = Field()
    a_site2: str = Field()

    class Config:
        schema_extra = {
            "example" : {
                "p_name": "정책 이름",
                "policy_id": "정책 번호",
                "introduction": "정책 요약",
                "policy_type": "정책 유형",
                "support": "지원 내용",
                "operating_period": "사업 운영 기간",
                "application_period": "사업 신청 기간",
                "scale": "지원 규모",
                "p_region": "관할 지역",
                "p_age_max": "최대 언령",
                "p_age": "언령",
                "p_region_income": "거주지 및 소득",
                "p_education": "학력",
                "p_major1": "전공",
                "p_employment": "취업 상태",
                "p_major2": "특화 분야",
                "detail": "추가 단서 사항",
                "restriction": "참여 제한 대상",
                "procedure": "신청 절차",
                "announcement": "심사 및 발표",
                "m_site": "신청 사이트",
                "document": "제출 서류",
                "etc": "기타 유익 정보",
                "a_name": "주관 기관",
                "m_name": "운영 기관",
                "a_site1": "사업 관련 참고 사이트1",
                "a_site2": "사업 관련 참고 사이트2"
            }
        }

class AsyncResponseModel(BaseModel):
    method : str = Field()
    link : str = Field()

    class Config:
        schema_extra = {
            "example" : {
                "message" : "To access the data, use below method",
                "method" : "GET",
                "link" : "href"
            }
        }

def AsyncResponse(status_code, method, link):
    return JSONResponse(status_code = status_code,
                        content = {
                            "message": "To access the data, use below method",
                            "method" : method,
                            "link" : link
                        })

def ResponseModel(data, message):
    return {
        "data" : [data],
        "message" : message
    }

def JSONResponseModel(status_code, message):
    return JSONResponse(status_code = status_code,
                        content = {
                            "message" : message
                        })


def ErrorResponseModel(message):
    return {
        "error" : "error",
        "message" : message
    }