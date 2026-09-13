import camera
import socket
import time

def init_camera():
    camera.init(0, format=camera.JPEG, framesize=camera.FRAME_SVGA)
    camera.quality(10)
    camera.flip(0)
    camera.mirror(0)

def build_index_page():
    return """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>ESP32-CAM - Coleta de Dataset</title>
</head>
<body style="text-align:center; font-family: sans-serif;">
    <h2>ESP32-CAM - Visualizacao ao vivo</h2>
    <img id="stream" src="/capture" style="max-width:90%;">
    <br><br>
    <button onclick="location.reload()">Atualizar imagem</button>
    <p>Acesse /capture para obter uma nova foto em JPEG.</p>
</body>
</html>"""

def handle_client(conn):
    request_line = conn.readline()
    while True:
        line = conn.readline()
        if not line or line == b"\r\n":
            break

    if request_line is None:
        conn.close()
        return

    path = request_line.split(b" ")[1] if b" " in request_line else b"/"

    if path.startswith(b"/capture"):
        buf = camera.capture()
        conn.send(b"HTTP/1.1 200 OK\r\n")
        conn.send(b"Content-Type: image/jpeg\r\n")
        conn.send(b"Content-Length: " + str(len(buf)).encode() + b"\r\n")
        conn.send(b"Connection: close\r\n\r\n")
        conn.send(buf)
    else:
        body = build_index_page().encode()
        conn.send(b"HTTP/1.1 200 OK\r\n")
        conn.send(b"Content-Type: text/html\r\n")
        conn.send(b"Content-Length: " + str(len(body)).encode() + b"\r\n")
        conn.send(b"Connection: close\r\n\r\n")
        conn.send(body)

    conn.close()

def start_server(port=80):
    init_camera()

    addr = socket.getaddrinfo("0.0.0.0", port)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print("Servidor HTTP da ESP32-CAM rodando na porta", port)

    while True:
        try:
            conn, client_addr = s.accept()
            print("Cliente conectado:", client_addr)
            handle_client(conn)
        except Exception as e:
            print("Erro ao atender cliente:", e)
            time.sleep(1)

start_server()
