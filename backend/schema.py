from pydantic import BaseModel

class LoginRequest(BaseModel):
    accounts: dict  # e.g. { "saba": {"username": "", "password": ""}, ... }

class BetRequest(BaseModel):
    platform: str
    match_id: int
    option: str
    amount: float
