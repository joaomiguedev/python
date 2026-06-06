import calculator
import temperature
import length
import mass
import coin
while True:
    print("1. calculator")
    print("2. temperature")
    print("3. length")
    print("4. mass")
    print("5. coin")
    print("6. exit")
    try:
        n1 = int(input("n1=:"))
    except ValueError:
        print("Enter numbers only!")
        continue
    if n1==1:
        calculator.opencalculator()
    elif n1==2:
        temperature.ontemperature()
    elif n1==3:
        length.onlength()
    elif n1==4:
        mass.onmass()
    elif n1==5:
        coin.oncoin()
    elif n1==6:
        break
    else:
        print("Invalid option!")
print("end")
