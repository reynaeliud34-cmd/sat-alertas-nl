import os
import time
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    datos = {
        "chat_id": CHAT_ID,
        "text": texto
    }
    requests.post(url, data=datos)

def revisar_citas():
    # Aquí después conectaremos la revisión de citas SAT
    return False

while True:
    try:
        if revisar_citas():
            enviar_mensaje("🚨 Hay una cita SAT disponible para e.firma persona física en Nuevo León")
        else:
            print("Sin citas disponibles")
    except Exception as e:
        print("Error:", e)

    time.sleep(300)  # 5 minutos
