import requests
import time
import sys
from requests.exceptions import RequestException, SSLError, ProxyError, Timeout, ConnectionError

REMOTE_MESSAGE_URL = "https://raw.githubusercontent.com/halilgultekin/my-python-app/main/message.txt"
LOCAL_FALLBACK = "local_message.txt"

def get_remote_message():
    try:
        r = requests.get(REMOTE_MESSAGE_URL, timeout=10)
        r.raise_for_status()  # HTTPError için
        return r.text.strip(), None
    except Exception as e:
        return None, e

def read_local_fallback():
    try:
        with open(LOCAL_FALLBACK, "r", encoding="utf-8") as f:
            return f.read().strip()
    except:
        return None

def main():
    print("🟢 Uygulama başladı. GitHub mesajı dinleniyor...\n")
    attempt = 0
    while True:
        msg, err = get_remote_message()
        if msg is not None:
            attempt = 0
            print("🔹 Uzaktaki mesaj:", msg)
        else:
            attempt += 1
            print("‼️ Uzaktan çekme hatası (deneme {}):".format(attempt))
            print("   Hata türü:", type(err).__name__)
            print("   Hata detayı:", str(err))
            # local fallback göster
            fallback = read_local_fallback()
            if fallback:
                print("   Yerel fallback mesaj:", fallback)
            else:
                print("   Yerel fallback yok.")
            # backoff: artan bekleme süresi
            wait = min(60, 5 * attempt)
            print(f"   {wait} saniye sonra tekrar denenecek...\n")
            time.sleep(wait)
            continue

        time.sleep(5)

if __name__ == "__main__":
    main()
