import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

RFC = os.getenv("SAT_RFC")
CURP = os.getenv("SAT_CURP")
EMAIL = os.getenv("SAT_EMAIL")


def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    datos = {
        "chat_id": CHAT_ID,
        "text": texto
    }
    requests.post(url, data=datos)


def revisar_citas():
    print("Iniciando revisión SAT...")
    
    print("RFC cargado:", bool(RFC))
    print("CURP cargado:", bool(CURP))
    print("Correo cargado:", bool(EMAIL))

    # Próximo paso: conectar con portal SAT
    return False


if __name__ == "__main__":
    if revisar_citas():
        enviar_mensaje("🚨 Cita SAT disponible para e.firma de personas físicas en Nuevo León")
    else:
        print("Revisión terminada")
