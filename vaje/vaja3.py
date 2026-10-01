import requests

vreme = requests.get("https://api.open-meteo.com/v1/forecast?latitude=46.0511&longitude=14.5051&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1")

klicjson = vreme.json()

print(f"{klicjson["current"]["temperature_2m"]}  °C")
