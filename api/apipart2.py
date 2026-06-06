import requests
print("0 - Euro\n1 - Dólar americano\n2 - Real brasileiro")
n1=int(input("n1: "))
print("0 - Euro\n1 - Dólar americano\n2 - Real brasileiro")
n2=int(input("n2: "))

def tradutor(val):
    if val==0:
        return "EUR"
    elif val==1:
        return "USD"
    elif val==2:
        return "BRL"
    else :
        return None

moeda1=tradutor(n1)
moeda2=tradutor(n2)

nome_do_API=f'http://economia.awesomeapi.com.br/json/last/{moeda1}-{moeda2}'
url=requests.get(nome_do_API)

data=url.json()
data_moeda=float(data[f'{moeda1}{moeda2}']['bid'])

moedainput=float(input(f"{moeda1}: "))

print(f"{moeda1} {moedainput} == {moeda2} {moedainput*data_moeda}")