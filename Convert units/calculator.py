def opencalculator():
    try:
        print(float(eval(input("calculator:"))))
    except ValueError:
        print("Enter numbers only!")
        return