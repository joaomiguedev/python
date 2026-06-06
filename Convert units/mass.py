import string
from time import sleep
def onmass():
    kg=0
    lbs=0
    para=str(input("kg,lbs:"))
    def kg_to_lbs(kg,lbs,para:string):
        if para=="kg":
            print(f"lbs {kg*2.20462262}.")
            sleep(1)
        elif para=="lbs":
            print(f"kg {lbs/2.20462262}")
            sleep(1)
    if para=="kg":
        try:
            kg=float(input("kg:"))
        except ValueError:
            print("Erro: enter a valid number.")
            return
        kg_to_lbs(kg,lbs,para)
    elif para=="lbs":
        try:
            lbs=float(input("lbs:"))
        except ValueError:
            print("Erro: enter a valid number.")
            return
        kg_to_lbs(kg,lbs,para)
    else:
        print("Invalid option!")
        sleep(1)