import http.client
import json
from config import settings


def call_to_number(phone_number: str):
    conn = http.client.HTTPSConnection(settings.api_url)
    payload = json.dumps({
        "messages": [
            {
                "destinations": [{"to":phone_number}],
                "from": "38515507799",
                "language": "en",
                "text": "Fire Alert, Fire Alert, Fire Alert!",
                "voice": {
                    "name": "Joanna",
                    "gender": "female"
                }
            }
        ]
    })
    headers = {
        'Authorization': f'App {settings.api_key}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/tts/3/advanced", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

