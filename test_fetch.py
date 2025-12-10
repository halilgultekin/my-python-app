import requests

URL = "https://raw.githubusercontent.com/halilgultekin/my-python-app/main/message.txt"

try:
    r = requests.get(URL, timeout=10)
    print("HTTP status:", r.status_code)
    print("First 300 chars of response:\n", r.text[:300])
except Exception as e:
    print("Exception:", type(e).__name__, str(e))
