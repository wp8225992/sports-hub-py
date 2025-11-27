class ImClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def login(self):
        # TODO: 实现IM平台登录逻辑
        pass
    def fetch_odds(self):
        # TODO: 实现获取盘口数据
        return [{"match_id": 301, "home": "E队", "away": "F队", "odds": {"E队": 1.7, "F队": 1.9}}]
    def place_order(self, match_id, option, amount):
        # TODO: 实现下注逻辑
        return {"success": True, "platform": "im"}