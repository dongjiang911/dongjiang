# FarmSense 智慧农场 App

可直接运行的智慧农场前端 Demo，重点演示“传感器数据接入 + 实时监测 + 告警 + 设备管理”。

## 已实现
- 农场总览：温度、空气湿度、土壤湿度、在线设备等核心指标
- 环境趋势图与区域健康度
- 传感器管理：设备状态、最新读数、新增设备
- 告警中心
- REST API / MQTT / WebSocket 接入说明
- Demo 模拟数据每 5 秒刷新

## 运行
```bash
python -m http.server 8080
```
然后访问 http://localhost:8080。

## 接入真实传感器
推荐架构：传感器 → IoT 网关 → MQTT/HTTP → 后端数据服务 → Web App。

示例：
```http
POST /api/v1/sensors/telemetry
Content-Type: application/json

{
  "deviceId": "TEMP-001",
  "timestamp": "2026-11-22T14:30:00Z",
  "metrics": {"temperature": 24.6, "humidity": 68, "soilMoisture": 42}
}
```

当前前端使用模拟数据；生产环境可把刷新逻辑替换成 `fetch('/api/v1/sensors/latest')` 或 WebSocket/MQTT 网关推送。