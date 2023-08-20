while True:
    temp=float(input("Enter the Temperature You want to convert: "))
    print("PRESS 1 to enter the temperature in Celsius to Fahrenheit.")
    print("PRESS 2 to enter the temperature in Fahrenheit to Celsius.")
    choice=int(input("Enter your Choise: "))

    if choice==1:
        cel=((temp-32)*5)/9
        print(cel)

    elif choice==2:
        fah=(1.8*temp)+32
        print(fah)

    else:
        exit



