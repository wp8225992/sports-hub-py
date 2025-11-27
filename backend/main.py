import uvicorn
from fastapi import FastAPI
from backend.manager import PlatformManager
from backend.schema import LoginRequest, BetRequest
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
manager = PlatformManager()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/login")
def api_login(req: LoginRequest):
    return manager.login_all(req.accounts)

@app.get("/api/odds")
def api_odds():
    return manager.get_all_odds()

@app.post("/api/bet")
def api_bet(req: BetRequest):
    return manager.place_bet(req.platform, req.match_id, req.option, req.amount)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)