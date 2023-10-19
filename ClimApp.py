import requests
import geocoder
import schedule
import time
from win10toast import ToastNotifier

notification = ToastNotifier()

URL_KEY = 'd5671ac4d774e125eee5eaf3e086813f'
UBICATION = geocoder.ip('me')
CITY = UBICATION.json['city']


def full_url():
    global UBICATION
    (lat, lng) = UBICATION.latlng
    URL = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lng}&exclude=minutely, hourly&units=metric&appid={URL_KEY}'
    return URL


URL_API = full_url()


def app():
    response = requests.get(URL_API)
    if response.status_code == 200:
        data = response.json()['daily'][0]['temp']
        actual_temp = data['day']
        title = f'El clima actual en {CITY} es de {actual_temp}°C'
        if actual_temp > 30 and actual_temp < 50:
            msg = 'Te recomiendo que uses ropa ligera como remeras o camisas y bermudas o shorts de verano, también podrías usar faldas. Evitaría usar jeans. Es opcional andar desnudo. Saludos! :)'
        elif actual_temp > 20 and actual_temp < 30:
            msg = 'Te recomiendo que uses jean o falda y remera mangas cortas. Opcional podrías llevar campera ligera. Hoy no hace tanto calor. Saludos loko :)'
        elif actual_temp > 10 and actual_temp < 20:
            msg = 'Te recomiendo una campera ligera o suéter. Remera mangas largas y jeans. Si querés usar faldas no te olvides de usar calzas. Hoy está fresquito, que tengas lindo día boludito. Aguante el frio carajo!!11'
        elif actual_temp > 0 and actual_temp < 10:
            msg = 'Hace un frío de la puta madre, así que te recomiendo un camperón y un buzo o suéter por debajo. Remera mangas largas y jeans o joggins ademas de un gorrito. Recordá ponerte mínimo 3 pares de medias. Saludos loko :)'
        elif actual_temp < 0:
            msg = 'Te recomiendo no salir de la cama☠️'
        else:
            msg = 'Procedé a pegarte un tiro antes de que mueras de calor XD'
        notification.show_toast(
            title,
            msg,
            icon_path='icon.ico',
            duration=6,
            threaded=True
        )
    else:
        print('Error', response.status_code)

schedule.every(4).hours.do(app)

while True:
    schedule.run_pending()
    time.sleep(1)