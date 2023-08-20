weight=float(input("Enter the weight: "))
height=float(input("Enter the height: "))

bmi=weight/(height*height)
print(bmi)

if bmi<18.5:
    print("You are underweight")
elif bmi>=18.5 and bmi<=25:
    print("Normal Weight")
elif bmi>=25 and bmi<=30:
    print("You are Overweight")

    
   
