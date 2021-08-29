import requests
import json

token = "c61a7afb831617d0863d6684d94e2369"
url = "https://marcelstein.com/elochallenge/getData.php?token=" + token

header = {"Host":"marcelstein.com",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
          "Accept":"application/json, text/plain, */*",
          "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
          "Accept-Encoding":"gzip, deflate, br",
          "Connection":"keep-alive"}

##print(url)
r = requests.get(url, headers=header)
rj = r.json()
#print(rj)

pedidos = open("pedidos.json", "w")

json.dump(rj, pedidos, indent=6)

pedidos.close()

