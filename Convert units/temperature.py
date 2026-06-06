import string
from time import sleep
def ontemperature():
    c=0
    f=0
    para=str(input("c,f:"))
    def ctof(c,f,para:string):
        if para=="c":
            print(f"f e {c*1.8+32}.")
            sleep(1)
        if para=="f":
            print(f"c e {(f-32)/1.8}.")
            sleep(1)
    if para=="c":
        try:
            c=float(input("c:"))
        except ValueError:
            print("Erro: introduz um número válido.")
            return
        ctof(c,f,para)
    if para=="f":
        try:
            f=float(input("f:"))
        except ValueError:
            print("Erro: introduz um número válido.")
            return
        ctof(c,f,para)
    else:
        print("Opção inválida!")
        sleep(1)