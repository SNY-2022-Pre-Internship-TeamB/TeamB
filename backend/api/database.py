import motor.motor_asyncio

MONGODB_URL = "mongodb://3.39.15.18:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client.SNdb
policy_collection = database.get_collection("resultAll")

def policy_name_helper(policy) -> dict:
    return {
        "p_name" : policy["p_name"]
    }

def policy_detail_helper(detail) -> dict:
    return {
        "introduction" : detail["introduction"],
        "policy_type" : detail["policy_type"],
        "support" : detail["support"],
        "p_region_income" : detail["p_region_income"],
        "detail": detail["detail"],
        "restriction": detail["restriction"],
        "procedure": detail["procedure"],
        "announcement": detail["announcement"],
        "m_site": detail["m_site"],
        "document": detail["document"],
        "etc": detail["etc"],
        "a_name": detail["a_name"]
    }

async def retrieve_policies(u_region, u_age, policy_type) -> dict:
    policies = []
    condition = {
        "p_region" : u_region,
        "p_age" : {"$lte" : u_age},
        "policy_type" : policy_type
    }
    async for policy in policy_collection.find(condition):
        policies.append(policy_name_helper(policy))
    print(policies)
    return policies

async def retrieve_details(policy_id) -> dict:
    details = []
    condition = {
        "policy_id" : policy_id
    }
    async for detail in policy_collection.find(condition):
        details.append(policy_detail_helper(detail))

    return details