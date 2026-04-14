#!/usr/bin/env python3
"""
大社区成本治理驾驶舱 - 局域网服务
用法:
    pip install flask
    python app.py
访问: http://<你的局域网IP>:8888
"""

import os
import socket
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".")

@app.route("/")
def index():
    return send_from_directory(".", "内帐下钻分析.html")

if __name__ == "__main__":
    def _local_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"

    ip = _local_ip()
    port = int(os.environ.get("PORT", 8888))
    print("=" * 55)
    print("  大社区成本治理驾驶舱")
    print("=" * 55)
    print(f"  本机访问:   http://localhost:{port}")
    print(f"  局域网访问: http://{ip}:{port}   ← 发给同事")
    print("=" * 55)
    app.run(host="0.0.0.0", port=port, threaded=True, debug=False)
