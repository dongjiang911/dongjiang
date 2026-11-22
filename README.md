# FarmSense 智慧农场 App

智慧农场 Web App + Python/FastAPI 传感器数据服务。

## 目录
- `index.html` / `styles.css` / `app.js`：前端 App
- `backend/main.py`：Python FastAPI IoT 数据服务
- `backend/requirements.txt`：Python 依赖

## 启动 Python 后端

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

API 默认运行在 `http://localhost:8000`。

## 启动前端

在项目根目录运行：

```bash
python -m http.server 8080
```

浏览器打开 `http://localhost:8080`。

前端会优先从 Python API 获取真实数据；API 不可用时自动使用演示数据。

## 传感器上报

```http
POST http://localhost:8000/api/v1/sensors/telemetry
Content-Type: application/json

{
  "deviceId": "TEMP-001",
  "timestamp": "2026-11-22T14:30:00Z",
  "metrics": {
    "temperature": 24.6,
    "humidity": 68,
    "soilMoisture": 42
  }
}
```

## 推荐真实硬件架构

传感器（ESP32/Arduino） → MQTT/HTTP → Python 数据服务 → Web App。

当前 Python 服务已经支持：
- 设备最新数据
- 历史遥测数据
- 健康检查
- 标准 JSON 遥测上报接口

下一步可以继续加入 MQTT（如 Mosquitto + Python MQTT client）、SQLite/PostgreSQL 历史存储，以及自动灌溉/风机/补光灯控制。