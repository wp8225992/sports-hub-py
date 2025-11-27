from backend.platform import clients

class PlatformManager:
    def __init__(self):
        self.instances = {}

    def login_all(self, accounts):
        for pname, account in accounts.items():
            if pname in clients:
                self.instances[pname] = clients[pname](**account)
                self.instances[pname].login()
        return {"status": "ok"}

    def get_all_odds(self):
        result = {}
        for pname, inst in self.instances.items():
            result[pname] = inst.fetch_odds()
        return result

    def place_bet(self, platform, match_id, option, amount):
        client = self.instances.get(platform)
        if client:
            return client.place_order(match_id, option, amount)
        return {"success": False, "error": "No client"}
