from datetime import datetime

import websocket
import json


def on_message(ws, message):
    print("Received message:", message)


def on_error(ws, error):
    print("Error:", error)


def on_close(ws):
    print("Connection closed")


def on_open(ws):
    connect_event = {
        "meta_event": {
            "type": "connect",
            "sub_type": "websocket"
        },
        "self_id": "your_self_id"
    }
    ws.send(json.dumps(connect_event))

    message = {
        "id": "121212112121",
        "self": {
            "platform": "qq",
            "user_id": "123234"
        },
        "time": 1632847927.599013,
        "type": "message",
        "detail_type": "private",
        "sub_type": "",
        "message_id": "6283",
        "message": [
            {
                "type": "text",
                "data": {
                    "text": "OneBot is not a bot"
                }
            }
        ],
        "alt_message": "OneBot is not a bot[图片]",
        "user_id": "123456788"
    }
    ws.send(json.dumps(message))


if __name__ == "__main__":
    # 指定WebSocket连接的地址
    ws_url = "ws://127.0.0.1:9154/onebot/v12/ws/"

    # 创建WebSocket连接
    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    # 运行WebSocket连接
    ws.run_forever(ping_interval=10, ping_timeout=5)
