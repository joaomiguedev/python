import requests
url=requests.get('http://economia.awesomeapi.com.br/json/last/EUR-USD')
data=url.json()
data_moeda=float(data['EURUSD']['bid'])
eur=float(input("EUR:"))
print(f"EUR {eur} == USD {eur*data_moeda}")