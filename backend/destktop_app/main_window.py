from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox, QMessageBox

import requests

API_URL = "http://127.0.0.1:8000"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("体育盘口聚合Demo")
        self.resize(500, 400)
        self.layout = QVBoxLayout(self)

        # 登录表单
        self.saba_user = QLineEdit(self)
        self.saba_user.setPlaceholderText("SABA账号")
        self.saba_pwd = QLineEdit(self)
        self.saba_pwd.setEchoMode(QLineEdit.Password)
        self.saba_pwd.setPlaceholderText("SABA密码")

        self.login_btn = QPushButton("登录所有平台")
        self.login_btn.clicked.connect(self.handle_login)

        self.layout.addWidget(QLabel("登录各平台"))
        self.layout.addWidget(self.saba_user)
        self.layout.addWidget(self.saba_pwd)
        self.layout.addWidget(self.login_btn)

        # 盘口区
        self.odds_btn = QPushButton("拉取全部盘口")
        self.odds_btn.clicked.connect(self.display_odds)
        self.odds_view = QTextEdit()
        self.odds_view.setReadOnly(True)
        self.layout.addWidget(self.odds_btn)
        self.layout.addWidget(self.odds_view)

        # 下单区
        self.platform_box = QComboBox()
        self.platform_box.addItems(["saba", "fb", "im"])
        self.match_id_inp = QLineEdit()
        self.match_id_inp.setPlaceholderText("比赛ID")
        self.option_inp = QLineEdit()
        self.option_inp.setPlaceholderText("下注选项")
        self.amount_inp = QLineEdit()
        self.amount_inp.setPlaceholderText("下注金额")
        self.bet_btn = QPushButton("下注")
        self.bet_btn.clicked.connect(self.place_bet)
        self.layout.addWidget(QLabel("下注"))
        self.layout.addWidget(self.platform_box)
        self.layout.addWidget(self.match_id_inp)
        self.layout.addWidget(self.option_inp)
        self.layout.addWidget(self.amount_inp)
        self.layout.addWidget(self.bet_btn)

    def handle_login(self):
        payload = {
            "accounts": {
                "saba": {
                    "username": self.saba_user.text(),
                    "password": self.saba_pwd.text()
                },
                # 可拓展其它平台
            }
        }
        r = requests.post(f"{API_URL}/api/login", json=payload)
        if r.ok:
            QMessageBox.information(self, "成功", "登录成功")
        else:
            QMessageBox.warning(self, "失败", "登录失败")

    def display_odds(self):
        r = requests.get(f"{API_URL}/api/odds")
        if r.ok:
            text = r.text
            self.odds_view.setPlainText(text)
        else:
            QMessageBox.warning(self, "错误", "获取盘口失败")

    def place_bet(self):
        try:
            payload = {
                "platform": self.platform_box.currentText(),
                "match_id": int(self.match_id_inp.text()),
                "option": self.option_inp.text(),
                "amount": float(self.amount_inp.text())
            }
        except Exception:
            QMessageBox.warning(self, "输入错误", "请检查下注参数")
            return
        r = requests.post(f"{API_URL}/api/bet", json=payload)
        if r.ok:
            QMessageBox.information(self, "下单结果", r.text)
        else:
            QMessageBox.warning(self, "错误", "下注失败")