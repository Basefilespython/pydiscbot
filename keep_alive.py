from os import system
try:
  from flask import Flask

except:
  system("pip3 install  flask")
  from flask import Flask
  
from threading import Thread

import json
import requests
ip = json.loads(requests.get("https://api.ipify.org/?format=json").text)['ip']

app = Flask(__name__)

@app.route('/')
def home():
  try:
   # data = get_info_by_ip() 
   #def get_info_by_ip():
    # ip = str(input())
    # ip = " ".join()
    if not ip:
        print("❗ Нет указан ip/домен")
    #  event.msg_op(2, "❗ Нет указан ip/домен")
    else:
        try:
            response = requests.get(
                url=f'http://ip-api.com/json/{ip}?lang=ru').json()

            if response.get("status") == "fail":
                data = "❌Информация не найдена. Проверьте данные!"
            else:
                data = f"""
                ⚙Айпи чекер⚙
                🔎IP: {response.get('query')}
                🤖Провайдер: {response.get('isp')}
                🌇Страна: {response.get('country')}
                🏙Регион: {response.get('regionName')}
                🏙Город: {response.get('city')}
                🔑Индекс: {response.get('zip') if response.get('zip') != "" else "Не найдено"}
                ✏Координаты: {response.get('lat')}:{response.get('lon')}""".replace(
                    "                ", "")
                # print(data)
        except Exception as err:
            data = err
            print(err)
        return data
  except Exception as err:
     data = "ЛОЛ",err  
  return data

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive_run():
  t = Thread(target=run)
  t.start()



if __name__ == "__main__":
    app.run()