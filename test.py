import requests
import time
import json

url = "https://discord.com/api/v9/invites/monad"
headers = {
    "Authorization": "",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "session_id": None
}

for i in range(999999):
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 400 or response.status_code == 403:
        try:
            error_message = response.json().get("message", "")
            if "invite is invalid" in error_message or "invite has expired" in error_message:
                print(f"Заявка номер {i + 1} була відхилена: {error_message}")
            elif "channel is full" in error_message:
                print(f"Заявка номер {i + 1} була відхилена через переповнений канал.")
            else:
                print(f"Заявка номер {i + 1} відхилена: {error_message}")
        except json.JSONDecodeError:
            print(f"Заявка номер {i + 1} не вдалося обробити: непізнаний формат відповіді.")
    else:
        print(f"Відправлений запит номер: {i + 1}, Статус-код: {response.status_code}")
    
    time.sleep(15)
