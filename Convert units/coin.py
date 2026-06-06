import string
import requests
from time import sleep
def oncoin():
    euro=0
    urd=0
    para=str(input("euro,urd:"))
    def euro_to_urd(euro,urd,para:string):
        if para=="euro":
            response = requests.get("https://api.frankfurter.app/latest?from=EUR&to=USD")
            data = response.json()
            rate = data["rates"]["USD"]
            print("Rate:", rate)
            print("USD:", (euro*rate))
            sleep(1)
        elif para=="urd":
            response = requests.get("https://api.frankfurter.app/latest?from=USD&to=EUR")
            data = response.json()
            rate = data["rates"]["EUR"]
            print("Rate:", rate)
            print("EUR:", (urd*rate))
            sleep(1)
    if para=="euro":
        try:
            euro=float(input("euro:"))
        except ValueError:
            print("Erro: enter a valid number.")
            return
        euro_to_urd(euro,urd,para)
    elif para=="urd":
        try:
            urd=float(input("urd:"))
        except ValueError:
            print("Erro: enter a valid number.")
            return
        euro_to_urd(euro,urd,para)
    else:
        print("Invalid option!")
        sleep(1)