import json
import requests

url = "https://marcelstein.com/elochallenge/sendresponse.php"
header = {"Accept": "application/json, text/plain, /",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "en-US,en;q=0.5",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive",
          "Content-Length": "8138",
          "content-type": "application/json",
          "Host": "marcelstein.com",
          "Origin": "https://marcelstein.com",
          "Pragma": "no-cache",
          "Referer": "https://marcelstein.com/elochallenge/starttest.php?token=c61a7afb831617d0863d6684d94e2369",
          "Sec-Fetch-Dest": "empty",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Site": "same-origin",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}


with open("C:/Users/Leo/Documents/UiPath/updateJson/jsonModificado.json", "r", encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)

#with open("C:/Users/Leo/PycharmProjects/rpaelo/pedidos.json", "r", encoding='utf-8-sig') as json_file:
#    json_data = json.load(json_file)

#print(json_data)

r = requests.post(url, headers=header, data=json_data)

#data=json.dumps(json_data)
print(r.text)
print(r.status_code)

