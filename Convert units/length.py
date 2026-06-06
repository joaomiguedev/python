import string
from time import sleep
def onlength():
    km=0
    miles=0
    para=str(input("km,miles:"))
    def km_to_miles(km,miles,para:string):
        if para=="km":
            print(f"miles {km/1.609344}.")
            sleep(1)
        elif para=="miles":
            print(f"km {miles*1.609344}.")
            sleep(1)
    if para=="km":
        try:
            km=float(input("km:"))
        except ValueError:
            print("Erro: enter a valid number.")
            return
        km_to_miles(km,miles,para)
    elif para=="miles":
        try:
            miles=float(input("miles:"))
        except ValueError:
            print("Erro: enter a valid number.")
            return
        km_to_miles(km,miles,para)
    else:
        print("Invalid option!")
        sleep(1)