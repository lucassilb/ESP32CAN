import network
import time

WIFI_SSID = "SUA_REDE_2.4GHZ"
WIFI_PASSWORD = "SUA_SENHA"

def connect_wifi():
    sta = network.WLAN(network.STA_IF)
    sta.active(True)

    if not sta.isconnected():
        print("Conectando ao Wi-Fi:", WIFI_SSID)
        sta.connect(WIFI_SSID, WIFI_PASSWORD)

        timeout = 20
        while not sta.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1

    if sta.isconnected():
        print("Wi-Fi conectado. IP:", sta.ifconfig()[0])
    else:
        print("Falha ao conectar ao Wi-Fi.")

    return sta

connect_wifi()
