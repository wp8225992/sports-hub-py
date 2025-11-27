# sports-hub-py

一个全栈Python开发的体育盘口聚合及自动下单桌面应用。
- 后端：FastAPI聚合各个平台盘口、下注API
- 桌面端：PySide6 (Qt for Python) 跨平台桌面UI
- 100% Python实现

## 目录结构概览

```
sports_hub_py/
├─ backend/         # FastAPI后端
│    ├─ platform/
│    ├─ main.py
│    ├─ schema.py
│    ├─ manager.py
├─ desktop_app/     # PySide6桌面端
│    ├─ main_window.py
│    ├─ app.py
├─ requirements.txt # 依赖文件
└─ README.md
```

## 运行方式（初步说明）

1. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
2. 启动后端（FastAPI）：
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
3. 启动桌面端：
   ```bash
   cd desktop_app
   python app.py
   ```

---