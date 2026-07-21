import os
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
    # Aquí después conectaremos la revisión del SAT
    return False

if __name__ == "__main__":
    if revisar_citas():
        enviar_mensaje("🚨 Cita SAT disponible para e.firma persona física en Nuevo León")
    else:
        print("Revisión completada: sin citas")
