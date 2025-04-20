#!/usr/bin/python
import socket
import time

# ファジングの初期設定
ip = "127.0.0.1"  # ターゲットIP
port = 9999  # ターゲットポート
timeout = 5  # タイムアウト秒数
initial_size = 100  # 最初のペイロードサイズ
step_size = 100  # 各ステップでバイト数を増やすサイズ
max_size = 3000  # 送信する最大バイト数

# バッファを段階的に増加させるための準備
buffer = ["A" * initial_size]  # 最初に100バイトの"A"を含むバッファ
while len(buffer[-1]) < max_size:
    buffer.append("A" * (len(buffer[-1]) + step_size))  # ステップごとにサイズを増加

# ファジング開始
for payload in buffer:
    size = len(payload)
    print(f"Fuzzing with {size} bytes...")

    try:
        # ソケット接続
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)  # タイムアウト設定
        s.connect((ip, port))
        
        # 初回の応答を受信
        s.recv(1024)

        # ペイロードを送信（バイト型に変換）
        s.send((payload + '\r\n').encode())

        # 応答を待つ
        response = s.recv(1024)
        print(f"Received response: {response}")

        s.close()
    except Exception as e:
        print(f"Error occurred with {size} bytes: {e}")
        break  # ここでエラーが発生したらループを終了（バッファオーバーフローの可能性）

    # 次のリクエスト送信前に少し待つ
    time.sleep(1)
