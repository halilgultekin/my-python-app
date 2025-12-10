import requests
import time

REMOTE_MESSAGE_URL = "https://raw.githubusercontent.com/KULLANICIADINIZ/REPOADI/main/message.txt"

def get_remote_message():
    try:
        r = requests.get(REMOTE_MESSAGE_URL, timeout=5)
        return r.text.strip()
    except:
        return "Bağlantı hatası!"

def main():
    print("🟢 Uygulama başladı. Remote mesaj okunuyor...\n")

    while True:
        msg = get_remote_message()
        print(f"🔹 Uzaktaki mesaj: {msg}")
        time.sleep(5)

if __name__ == "__main__":
    main()
