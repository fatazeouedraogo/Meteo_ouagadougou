import requests
import matplotlib.pyplot as plt
import datetime


API_KEY = '465961c262e1a4d66cd5d2a66cdfaf9e'
VILLE = 'Ouagadougou'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={VILLE}&appid={API_KEY}&units=metric'

def recuperer_meteo():
    reponse = requests.get(URL)
    data = reponse.json()
    dates = []
    temperatures = []
    for item in data['list']:
        dates.append(datetime.datetime.fromtimestamp(item['dt']))
        temperatures.append(item['main']['temp'])
    return dates, temperatures

def tracer_graphique(dates, temperatures):
    plt.figure(figsize=(10,5))
    plt.plot(dates, temperatures, marker='o')
    plt.title(f'Températures prévues à {VILLE} (prochaines 5 jours)')
    plt.xlabel('Date et heure')
    plt.ylabel('Température (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    dates, temps = recuperer_meteo()
    tracer_graphique(dates, temps)
