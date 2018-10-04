import os
import json
from urllib.parse import urlencode
from urllib.request import urlopen
from datetime import datetime

API_ID = os.getenv('OWM_API_ID')
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def lambda_handler(event: dict, context):
    if not API_ID:
        print('ERROR: No API ID')
        return

    # get whether information from OpenWeatherMap
    url = 'https://api.openweathermap.org/data/2.5/weather?{}'.format(urlencode({
        'q': 'Ho Chi Minh City,VN',
        'units': 'metric',
        'appid': API_ID
    }))
    with urlopen(url) as f:
        raw_data = json.loads(f.read().decode('utf-8'))

    # raw_data = json.loads('''{
    #     "coord": {
    #     "lon": 106.7,
    #     "lat": 10.78
    #     },
    #     "weather": [
    #     {
    #       "id": 802,
    #       "main": "Clouds",
    #       "description": "scattered clouds",
    #       "icon": "03n"
    #     }
    #     ],
    #     "base": "stations",
    #     "main": {
    #     "temp": 28,
    #     "pressure": 1008,
    #     "humidity": 83,
    #     "temp_min": 28,
    #     "temp_max": 28
    #     },
    #     "visibility": 10000,
    #     "wind": {
    #     "speed": 2.1,
    #     "deg": 250
    #     },
    #     "clouds": {
    #     "all": 40
    #     },
    #     "dt": 1538314200,
    #     "sys": {
    #     "type": 1,
    #     "id": 7985,
    #     "message": 0.0058,
    #     "country": "VN",
    #     "sunrise": 1538260921,
    #     "sunset": 1538304244
    #     },
    #     "id": 1566083,
    #     "name": "Ho Chi Minh City",
    #     "cod": 200
    # }''')

    print('Location: {}, {}'.format(raw_data['name'], raw_data['sys']['country']))
    print('Time: {}'.format(datetime.fromtimestamp(raw_data['dt']).strftime(DATETIME_FORMAT)))
    print('Weather: {}, {}'.format(raw_data['weather'][0]['main'], raw_data['weather'][0]['description']))
    print('Temperature: {}℃'.format(raw_data['main']['temp']))
    print('Pressure: {:,}hPa'.format(raw_data['main']['pressure']))
    print('Humidity: {}%'.format(raw_data['main']['humidity']))


if __name__ == '__main__':
    lambda_handler({}, None)
