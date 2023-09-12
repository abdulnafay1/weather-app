import pip
pip.main(['install','requests'])
import requests

API_KEY = '1fd55aa66d50cbdbc4225e320c55b127'

def get_weather(city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, API_KEY)
    response = requests.get(base_url)
    data = response.json()

    if data['cod'] == 200:
        weather_info = {
            'City': data['name'],
            'Temperature (Celsius)': round(data['main']['temp'] - 273.15, 2),
            'Description': data['weather'][0]['description'],
            'Humidity (%)': data['main']['humidity'],
            'Wind Speed (m/s)': data['wind']['speed']
        }
        return weather_info
    else:
        return None


def main():
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name)

    if weather_data:
        print("\nWeather in {}: ".format(city_name))
        for key, value in weather_data.items():
            print("{}: {}".format(key, value))
    else:
        print("City not found. Please try again.")


main()
